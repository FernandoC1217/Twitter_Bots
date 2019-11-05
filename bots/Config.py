# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv('uw9LFBUG68eTQ9WbOxDqIceNr')
    consumer_secret = os.getenv('XZbN2YE6teESsBjRNY2AG9JYhbvPqmvv798rIejM4Lg9xdWmhd')
    access_token = os.getenv('4492109894-vMXUD1of3x3CacjPVn4sikXEnGuNDwuwjZjVn2d')
    access_token_secret = os.getenv('xDm3uliQkViSfKn4XgFcmXjkzhwL6w5pmcXUEhoN7C2uu')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api





