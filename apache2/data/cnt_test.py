import pandas as pd


def count_plus(name):
    df = pd.read_csv("./data/total_disease2_count_FINAL.csv", encoding="cp949")
    count = df.loc[df[df['title'] == name].index[0]]['count']
    df.loc[df['title'] == name, 'count'] = count + 1
    df.to_csv("./data/total_disease2_count_FINAL.csv", encoding="cp949", index=False)
