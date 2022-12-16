import line
import re
import snscrape.modules.twitter as sntwitter
import pandas as pd


def get_retweets(retweet_number, twitter_user_name):
    query = "(from:{}) until:2022-01-01 since:2010-01-01".format(twitter_user_name)
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == retweet_number:
            break
        else:
            tweets.append([tweet.content])

    df = pd.DataFrame(tweets, columns=['Tweet'])
    df.to_csv('tweets.csv')


def print_tweets():
    words = re.split(r"[^A-Za-z]", line.strip())
    for word in words:
        print(word)


if __name__ == "__main__":
    get_retweets(1000, "TWITTER_USER_NAME")
    print_tweets()
