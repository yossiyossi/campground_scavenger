import random
import time
from datetime import datetime
import tweepy
from apps.scavenger import check
import json

CAMPGROUNDS = "231959"  # plaskett
START_DATE = "2021-04-24"
END_DATE = "2021-04-25"

# twitter stuff
USER_TO_TWEET_AT = 'yossiberg'
CREDENTIALS_FILE = "twitter.json"
MAX_TWEET_LENGTH = 279
with open(CREDENTIALS_FILE) as f:
    tc = json.load(f)
print('using tc: ', tc)
print('campgrounds searching for: ', CAMPGROUNDS)
print('start date: ', START_DATE)
print('end date: ', END_DATE)


def create_tweet(totweet):
    totweet = totweet[:MAX_TWEET_LENGTH]
    my_auth = tweepy.OAuthHandler(tc["consumer_key"], tc["consumer_secret"])
    my_auth.set_access_token(tc["access_token_key"], tc["access_token_secret"])
    my_api = tweepy.API(my_auth)

    resp = my_api.update_status(status=totweet)
    # api.CreateFavorite(resp)
    print("The following was tweeted: ")
    print()
    print(totweet)
    print("response: ", resp)


SUCCESS = False
while not SUCCESS:
    try:
        results, start_string, end_string = check.master_scraping_routine(CAMPGROUNDS.split(),
                                                                          START_DATE,
                                                                          END_DATE)  # have to split
        print("{} -- start to end: {} to {}, results: {}".format(datetime.now(), start_string, end_string, results))

        for result in results:
            if result.get('success') is True:
                SUCCESS = True
                print('GOT A SUCCESS ***************************************')
                tweet = "@{}!!! ".format(USER_TO_TWEET_AT)
                tweet += "you dumbo, the campsite is available now \n"
                tweet += result.get('availability')
                tweet += "{}, {}".format(start_string, end_string)
                tweet += "\n 🏕🏕🏕\n"
                tweet += "\n" + "🏕" * random.randint(5, 50)  # To avoid duplicate tweets.
                create_tweet(tweet)
        time.sleep(10)
    except Exception as e:
        print("exception happened, printing and continuing: ", e)

