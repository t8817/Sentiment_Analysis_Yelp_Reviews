#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2020/4/23 23:46
#@Author  :Millie Zeng
#@FileName: Classier_Treee.py
#@Software: VScode

import json
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore') #ignore those warnings
stop_words = set(stopwords.words("english"))  #create a stop_words set


def cal_sentiment(text):
    #NLTK word tokenizer(split text into words)
    word_tokens = word_tokenize(text)  
    #delete unnecessary words(stop_words)
    word_tokens=[word for word in word_tokens if word not in stop_words]  
    # basic classifier
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

def main():
    result={}
    index=0
    with open("data/data3.json", 'r') as load_f:  #load in json file
        load_dict = json.load(load_f)
        for item in load_dict:
            text=item['text'] #select 'text' column
            text=text.lower() #lowercase of text
            text=text.replace('\n','')  #delete \n 
            sentiment=cal_sentiment(text)  #start classifier (calculate sentiment type)
            print(sentiment+'\t'+text) #make table
            item['sentiment']=sentiment #create a column 'sentiment'
            result[index]=item #make index
            index+=1
    result=pd.DataFrame(result).T #create a new table
    result.to_excel('sentiment3.xlsx',index=None)  #save results

if __name__ == '__main__':
    main()