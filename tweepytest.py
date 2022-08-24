import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("SFNRcHJIUlJ2Wkg5d2pLY04yWmc6MTpjaQ", 
    "iREXF66fNiLcQtDWmcEZ2Z1figHcWk5wtiSxWZyOHjPxegx0_d")
auth.set_access_token("821452134071812100-WQ9pXyAWbA6ovv8geMU6KGne28MFFEU", 
    "XeTZfXPkJ0HqKP2u6LAFsNgaLZiGPL5wWg6vNtNI1jkCc")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")