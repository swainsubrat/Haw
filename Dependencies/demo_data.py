"""
Structures dataframes for plotting
"""
import re
import pandas as pd
from io import StringIO
from pandas.core.frame import DataFrame


def DataFrameBuilder(FILE: StringIO) -> dict:
    DF = {}

    def basicDataFrameBuilder() -> DataFrame:
        lines = FILE.readlines()
        list_df = []
        for line in lines:
            line = line.rstrip('\n').split(" - ")
            if re.search(r"\d\d\/\d\d\/\d\d, (\d\d|\d):\d\d (pm|am)", line[0]):
                name_message = line[1].split(": ")
                if len(name_message) <= 1:
                    continue
                date, time = line[0].split(", ")
                name = name_message[0]
                message = ""
                for i in range(1, len(name_message)):
                    message += name_message[i]
                list_df.append([date, time, name, message])
            else:
                for item in line:
                    list_df[-1][-1] += item

        df = DataFrame(list_df, columns=['Date', 'Time', 'Name', 'Message'])
        df['Day'] = pd.DatetimeIndex(df['Date']).day
        df['Month'] = pd.DatetimeIndex(df['Date']).month
        df['Month_Year'] = pd.to_datetime(df['Date']).dt.to_period('M')
        df['Year'] = pd.DatetimeIndex(df['Date']).year
        return df

    def messageDataFrameBuilder(df: DataFrame, TOP: int=10) -> DataFrame:
        dfm = df.groupby('Name').Message.count().\
                     reset_index(name="Message Count")
        dfm.sort_values(
            by="Message Count",
            ascending=False,
            inplace=True,
            ignore_index=True
        )
        dfm.loc[dfm.index >= TOP, 'Name'] = 'Others'
        dfm = dfm.groupby(
            "Name"
            )["Message Count"].sum().reset_index(name="Message Count")
        dfm.sort_values(
            by="Message Count",
            ascending=False,
            inplace=True,
            ignore_index=True)
        dfmD = df.groupby('Date').Message.count().\
            reset_index(name='Count')
        dfmMY = df.groupby('Month_Year').Message.count().\
            reset_index(name='Count')
        dfmY = df.groupby('Year').Message.count().\
            reset_index(name='Count')

        return dfm, dfmD, dfmMY, dfmY

    def emojiDataFrameBuilder(df: DataFrame, TOP: int=10) -> DataFrame:
        import emoji
        total = 0
        count = {}
        emoji_cnt = []
        for message in df['Message']:
            emoji_cnt.append(emoji.emoji_count(message))
            emoji_list = emoji.emoji_lis(message)
            for item in emoji_list:
                if (item["emoji"] in count):
                    count[item["emoji"]] += 1
                else:
                    count[item["emoji"]] = 1
            total += emoji.emoji_count(message)

        columns = ['Emojis', 'Count']
        dfe = pd.DataFrame(columns=columns)
        for key, value in count.items():
            data = {'Emojis': key, 'Count': value}
            dfe = dfe.append(data, ignore_index=True)
        dfe.sort_values(by="Count",
                        ascending=False,
                        inplace=True,
                        ignore_index=True)
        dfe.loc[dfe.index >= TOP, 'Emojis'] = 'Others'
        dfe = dfe.groupby("Emojis")["Count"].sum().reset_index(name="Count")
        df.insert(loc=6, column='Emoji Count', value=emoji_cnt)
        dfeD = df.groupby('Date')['Emoji Count'].sum().\
            reset_index(name='Count')
        dfeMY = df.groupby('Month_Year')['Emoji Count'].sum().\
            reset_index(name='Count')
        dfeY = df.groupby('Year')['Emoji Count'].sum().\
            reset_index(name='Count')

        dfeg = df.groupby('Name')['Emoji Count'].sum().\
            reset_index(name="Count")
        dfeg.sort_values(
            by="Count",
            ascending=False,
            inplace=True,
            ignore_index=True
        )
        dfeg.loc[dfeg.index >= TOP, 'Name'] = 'Others'
        dfeg = dfeg.groupby("Name")["Count"].sum().reset_index(name="Count")

        return dfe, dfeD, dfeMY, dfeY, dfeg

    DF['df'] = basicDataFrameBuilder()
    DF['dfm'], DF['dfmD'], DF['dfmMY'], DF['dfmY'] = \
        messageDataFrameBuilder(df=DF['df'], TOP=10)
    DF['dfe'], DF['dfeD'], DF['dfeMY'], DF['dfeY'], DF['dfeg'] = \
        emojiDataFrameBuilder(df=DF['df'], TOP=10)

    return DF