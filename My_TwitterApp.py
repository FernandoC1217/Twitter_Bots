import tweepy

#Add your credentials here
twitter_keys = {
        'consumer_key':        'uw9LFBUG68eTQ9WbOxDqIceNr',
        'consumer_secret':     'XZbN2YE6teESsBjRNY2AG9JYhbvPqmvv798rIejM4Lg9xdWmhd',
        'access_token_key':    '4492109894-vMXUD1of3x3CacjPVn4sikXEnGuNDwuwjZjVn2d',
        'access_token_secret': 'xDm3uliQkViSfKn4XgFcmXjkzhwL6w5pmcXUEhoN7C2uu'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

user = api.get_user("RainbowcolorXd")

 # Methods for Users: Get the user name, description, location and his/her last followers
print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)






