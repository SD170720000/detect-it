import tweepy
import authentication

api = tweepy.API(authentication.auth, wait_on_rate_limit=True)
