from twitter import OAuth, Twitter

from apps.scavenger import check
import json
import twitter

# twitter stuff
CREDENTIALS_FILE = "twitter.json"
MAX_TWEET_LENGTH = 279
with open(CREDENTIALS_FILE) as f:
    tc = json.load(f)


def create_tweet(tweet):
    tweet = tweet[:MAX_TWEET_LENGTH]
    tweeter = Twitter.Api(auth=OAuth(
        token=tc["todo"],
        token_secret=tc["todo"],
        consumer_key=tc["consumer_key"],
        consumer_secret=tc["consumer_secret"],
    ))
    resp = tweeter.PostUpdate(tweet)
    # api.CreateFavorite(resp)
    print("The following was tweeted: ")
    print()
    print(tweet)


CAMPGROUNDS = "231959"  # plaskett
START_DATE = "2021-04-23"
END_DATE = "2021-04-25"

results, start_string, end_string = check.master_scraping_routine(CAMPGROUNDS.split(),
                                                                  START_DATE,
                                                                  END_DATE)  # have to split
print(results)
print(start_string)
print(end_string)
