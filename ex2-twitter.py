import tweepy  
import time
import json

#credenciais de acesso
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"  

#criação de um objeto api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)

#requisições GET
user = api.get_user(screen_name = 'UTFPR_')  
print("Nome do usuario:" + user.name)
user = api.get_user(screen_name = 'UTFPR_')  
print("Quantidade de seguidores:", user.followers_count)  
print("Quantidade de amigos:", user.friends_count)
print('Local: ' + user.location)

try:  
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="UTFPR_", exclude_replies=True, count = 10).items(20):  
                    tweet_text = tweet.text  
                    time = tweet.created_at  
                    tweeter = tweet.user.screen_name  
                    tweet_dict = {"TWEET" : tweet_text.strip(), "TIMESTAMP" : str(time), "USUARIO" :tweeter}  
                    tweet_json = json.dumps(tweet_dict)  
                    print(tweet_json)  
except tweepy.TweepError:  
    time.sleep(60)


