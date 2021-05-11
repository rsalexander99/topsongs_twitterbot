#!/usr/bin/env python3

import tweepy
import requests
import spotipy
import pandas as pd
import time

df = pd.read_csv("Spotify_IDs.csv") # Read in Spotify Artist ID data
groupname_lst = df["Kpop_Groupname"].to_list() # Coerce K-pop Group column into list

# Authorize connection to Twitter API
consumer_key = "xxxxxxxxx" # Set keys
consumer_secret = "xxxxxxxxx"
access_token = "xxxxxxxxx"
access_token_secret = "xxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) # Establish connection object
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Authorize connection to Spotify API
client_id = "xxxxxxxxx" # Set keys
client_secret = "xxxxxxxxx"

auth_url = "https://accounts.spotify.com/api/token" 
auth_response = requests.post(auth_url, { # Establish connection object
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})

auth_response_data = auth_response.json() # Convert connection response to JSON
access_token = auth_response_data['access_token'] # Save the access token
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token) # Format access token to suit header for upcoming CRUD request
}

base_url = 'https://api.spotify.com/v1/artists/' # Specify entrypoint for artist ID for upcoming CRUD request

# Track latest tweet ID: Store in external txt file method
# Read in latest tweet ID
def retrieve_latest_id(file_name):
    f_read = open(file_name, 'r')
    latest_id = int(f_read.read().strip())
    f_read.close()
    return latest_id # Store latest tweet ID
# Update latest tweet ID 
def store_latest_id(latest_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(latest_id)) # Overwrite former latest tweet ID with new latest tweet ID
    f_write.close()
    return

# Reply to mentions
def reply_to_tweets():
    # Access latest tweet ID from file
    latest_id = retrieve_latest_id('latest_id.txt')
    # Store metadata on each mention into list variable
    mentions = api.mentions_timeline(latest_id)
    for mention in reversed(mentions): # Iterate backwards; respond to oldest tweets first
        # Extract text
        tweet = mention.text
        # Initialize key-word indicator, remains False as long as key-word is not Found
        found = False
        for name in groupname_lst: # Select K-pop group names
            if name.lower() in tweet.lower().replace(r'[^\w\s]+', ' '): # Check if K-pop group name is in tweet string
                # Pull Spotify artist ID from df
                artist_row = df[df['Kpop_Groupname'].str.lower() == name.lower()]
                artist_id =  artist_row['Spotify_ID'].to_string(index=False).strip()
                # Pull data on artist's top tracks
                r = requests.get(base_url + artist_id + '/top-tracks', 
                    headers=headers, 
                    params={'market': 'US'})
                d = r.json()
                found = True # Update key-word indicator
        if found:
            top3 = d['tracks'][0]['name'] + "\n" + d['tracks'][1]['name'] + "\n" + d['tracks'][2]['name'] # Extract names of Top 3 tracks
            api.update_status(("@" + mention.user.screen_name + "\n" + top3), mention.id) # Reply to tweet
        if not found and 'help' not in tweet.lower():
            error_msg = "K-pop group not found. The group you are searching for may no longer be active, or is unknown to this bot's creator. Tweet 'help' for more information."
            api.update_status(("@" + mention.user.screen_name + "\n" + error_msg), mention.id) # Reply to tweet
        # If 'help' key-word is found
        if 'help' in tweet.lower():
            directions = "Tweet this bot the name of a K-pop group to find out their Top 3 currently most-popular tracks! Please leave out any spacing or punctuation in the K-pop group's name."  
            api.update_status(("@" + mention.user.screen_name + "\n" + directions), mention.id) # Reply to tweet
        # Save newer latest tweet ID
        latest_id = mention.id
        # Store newer latest tweet ID into file
        store_latest_id(latest_id, 'latest_id.txt')

# Run function every 30 seconds
while True:
    reply_to_tweets()
    time.sleep(30)
