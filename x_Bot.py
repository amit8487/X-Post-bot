import tweepy
import requests


api_Key = "api key"
api_key_Secret = "secret key"
access_Token = "access token"
access_Token_Secret = "token secret"



def post(joke):
    if not joke:
        print("sorry there is no joke...")
        return None

def post(joke):
    if not joke:
        print("Sorry, there is no joke...")
        return

    try:
        
        client = tweepy.Client(
            consumer_key=api_Key,
            consumer_secret=api_key_Secret,
            access_token=access_Token,
            access_token_secret=access_Token_Secret
        )
        
        
        response = client.create_tweet(text=joke)
        
        # Check if the post was successful
        if response.data and response.data.get('id'):
            print(f"✅ Successfully posted tweet ID: {response.data['id']}")
            print(f"Posted Joke: {joke}")
        else:
            print("⚠️ Post failed, but no specific error was returned by X.")


    except tweepy.TweepyException as e:
        print(f"❌ Error posting to X (Tweepy Exception): {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def get_jokes():
    url = "https://v2.jokeapi.dev/joke/Any"
    data = requests.get(url)
    jd = data.json()

    if(data.status_code == 200):
        if(jd["type"] == "single"):
            
            joke = f"{jd["joke"]}"
            #print(sk)
            post(joke)
            return
        
        elif(jd["type"] == "twopart"):
            joke = f"{jd["setup"]} \n{jd["delivery"]}"
            post(joke)
            #print(joke)
            return
        else:
            raise Exception("failed")
    else:
        raise Exception("Faild to fatch jokes...")
            
    

def main():
    get_jokes()

if __name__ == "__main__":
    main()