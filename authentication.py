import tweepy
import tokenization as token

auth = tweepy.OAuthHandler(token.api_key, token.api_key_secret)
auth.set_access_token(token.access_token, token.access_token_secret)