import tweepy
import keys 

def api():
    auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)
    
    return tweepy.API(auth)

def tweet (api: tweepy.API, message: str, image_path:None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else: 
        api.update_status(message)
        
    print('tweeted_successfully')

if __name__ == "__main__": 
    api = api()
    tweet(api, 'Mathematical!', None)