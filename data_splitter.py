# author: Tanvi Kulkarni
import json
import csv
import io
import os
import arff
import pandas as pd

reviewFile = open('review.json', encoding="utf8")

file_num = 0

def save_data(review_save_data, file_num=0):
    file_name = 'review' + str(file_num) + '.json'
    with open(file_name, 'w', encoding="utf-8") as review_write:
         json.dump(review_save_data, review_write)

count = 1
review_data = list()
for i, line in enumerate(reviewFile):
    if(count%1000==0):
        print(str(count) + " done")
    count += 1
    data = json.loads(line)
    business_id = str(data["business_id"])
    review_id = str(data["review_id"])
    stars = str(data["stars"])
    text = str(data["text"]) if data["text"] is not None else "null"
    review_data.append([business_id, review_id, stars, text])
    if (count % 100000 == 0):
        # save data
        save_data(review_data, file_num)
        file_num += 1
        review_data.clear()

save_data(review_data, file_num)
reviewFile.close()
