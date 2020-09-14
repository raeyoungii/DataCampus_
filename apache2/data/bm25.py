#!/home/woongsup/anaconda3/bin/python
from cdqa.retriever import BM25Retriever
import konlpy 
from konlpy.tag import Mecab
import pandas as pd
import numpy as np
from classification import stop_word, classification_
from collections import OrderedDict

def get_ans(query1, depart):
    df = pd.read_csv("./data/total_disease2_count_FINAL.csv", encoding='cp949').fillna('Null')
    df.rename(columns = {'symptoms': 'content'}, inplace = True)

    if depart != "없음":
        df = df[df["subject"].isin([depart])].reset_index()
    else:
        df = df[df["subject"].isin(classification_(query1))].reset_index()
    retriever = BM25Retriever(lowercase=False,
                            tokenizer = stop_word
                            )
    retriever.fit(df)
    query1 = " ".join(stop_word(query1))
    rp = retriever.predict(query1)
    for i in rp:
        rp[i] = float(rp[i]) * df.iloc[i]['count']
        
    rp = OrderedDict(sorted(rp.items(), key=lambda x: x[1], reverse=True))

    top_5 = list(rp.keys())[:5]
    list_score = list(map(float,list(rp.values())))[:5]

    if list_score[0] != 0:
        percent_score = [round((i / sum(list_score)) ,2) * 100 for i in list_score]
    else:
        percent_score = [20 for _ in range(5)]

    top_5_df = df.iloc[top_5,[0,1,2]]
    top_5_df["score"] = percent_score
    return top_5_df
