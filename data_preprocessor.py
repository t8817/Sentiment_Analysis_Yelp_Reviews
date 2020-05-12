# author: Tanvi Kulkarni
import json
import pandas as pd

# stop = 100000
businessFile = open('yelp_business.json', encoding="utf8")

business_data = list()
for i, line in enumerate(businessFile):
    # convert the json on this line to a dict
    # if i % 10000 == 0:
    #     print(i)
    # if i == stop:
    #     break
    data = json.loads(line)
    # extract what we want
    business_id = data["business_id"]
    name = data["name"]
    stars = data["stars"]
    is_open = data["is_open"]
    # add to the data collected so far
    business_data.append({'business_id':business_id, 'name':name, 'stars':stars, 'is_open':is_open})

with open('business.json', 'w') as business:
    json.dump(business_data, business)

# df = pd.DataFrame(business_data, columns=['business_id', 'name', 'stars', 'is_open'])
businessFile.close()

# reviewFile = open('yelp_review.json', encoding="utf8")
#
# review_data = list()
# for i, line in enumerate(reviewFile):
#     # convert the json on this line to a dict
#     data = json.loads(line)
#     # extract what we want
#     business_id = data["business_id"]
#     review_id = data["review_id"]
#     user_id = data["user_id"]
#     stars = data["stars"]
#     text = data["text"]
#     print(text)
#     # add to the data collected so far
#     review_data.append({'business_id':business_id, 'review_id':review_id, 'user_id':user_id, 'stars':stars, 'text':text})
#
# with open('review.json', 'w') as review:
#     json.dump(review_data, review)
#
# reviewFile.close()