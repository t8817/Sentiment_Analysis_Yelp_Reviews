#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2020/4/23 23:46
#@Author  :Millie Zeng, Tanvi
#@FileName: Classier_Treee.py
#@Software: VScode

import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')
stop_words = set(stopwords.words("english"))  #停用词词表


def cal_sentiment(text):
    word_tokens = word_tokenize(text)  #NLTK分词
    word_tokens=[word for word in word_tokens if word not in stop_words]  #delete unnecessary words
    # classification tree
    if 'worst' in word_tokens:
        sentiment='neg'
    else:
        if 'horrible' in word_tokens:
            sentiment='neg'
        else:
            if 'great' in word_tokens:
                sentiment='pos'
            else:
                if 'delicious' in word_tokens:
                    sentiment='pos'
                else:
                    if 'prefect' in word_tokens:
                        sentiment='pos'
                    else:
                        if 'terrible' in word_tokens:
                            sentiment='neg'
                        else:
                            sentiment='neu'
    return sentiment

def getTheSentiments(i):
    result={}
    index=0
    with open("review"+str(i)+".json", 'r') as load_f:  #load in json file
        load_dict = json.load(load_f)
        for item in load_dict:
            text=item['text']
            text=text.lower() #lowercase of text
            text=text.replace('\n','')  #delete \n 
            sentiment=cal_sentiment(text)  #calculate sentiment type
            # print(sentiment+'\t'+text)
            item['sentiment']=sentiment
            result[index]=item
            index+=1
    result=pd.DataFrame(result).T
    result.to_excel('sentiment'+str(i)+'.xlsx',index=None)  #save results

def main():
    for i in range(0, 11):
        getTheSentiments(i)
    print("sentiment done")

if __name__ == '__main__'
    main()