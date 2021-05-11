# topsongs_twitterbot
Tweet a K-pop group's name to @kpop_topsongbot to find out what tracks are trending from your favs!

This bot extracts data from Spotify's Web API to return the Top 3 currently most popular songs by the user's requested K-pop group.

## How to Use:

Tweet the name of any K-pop group, and tag the twitter handle, @kpop_topsongbot in your tweet. You can simply tweet the name of the group you are interested in, or you can tweet a complete question which includes that group's name, such as:
- "What's the latest from Cravity?" or, 
- "What songs are trending by BTS?" 

My favorite K-pop groups are BTS, DAY6, and Mamamoo, and I would encourage anyone unfamiliar with K-pop to check them out! For K-pop groups with punctuation and spacing in their name, tweet the group's name without those additional characters. For example:
- "NCT 127" becomes "NCT127"
- "N'UEST" becomes "NUEST" 

To access these directions on Twitter, tweet 'help' to the bot. Do not worry about capitalization, the bot will still recognize group names which may be incorrectly capitalized in the user's mention. Additionally, this bot only returns song data on still-active K-pop groups. Groups which have disbanded will not be recognized.

## How it Works:

Spotify assigns every song a popularity rating according to the number of plays it as, as well as how recent those plays are. This bot connects to the Spotify Web API to access metadata on the Top 10 most popular songs by the artist specified in the tweet mention. The spotipy library is used to interact with the Spotify API, and the tweepy library is used to interact with the Twitter API. To call the correct Spotify endpoint to access data on the artist's top tracks, this bot's script uses the pandas library to pull the artist ID string of the specified K-pop group from a local csv file mounted to the container running on EC2. I personally compiled this csv, including all the K-pop artists I could think of, so if an existing, still-active, and correctly specified K-pop group is not found by this bot, it is because I have never heard of them. (*Correction: Blackpink will not be recognized by this bot, despite being a internationally well-known group. I accidently forgot to include them in my local csv file.*)

This bot access the most recent user mentions by storing the user's tweet ID in a text file mounted to the container. This bot's script reads in this text file, extracts the last tweet ID from the last time the script was run, and then updates that text file with the most recent tweet ID, extracted during the script's latest run.

This bot deploys every 30 seconds, so it will take up to 30 seconds for a user's mention to recieve a reply. 

## Project Reflections

I relied heavily on articles and video tutorials explaining how to use tweepy and spotipy. I had trouble figuring out the correct parameters to pass for some of the functions I used, specifically in my get request for the artist's top tracks. After some experimentation, I realized to set the market to the United States, so it would be appropriate to specify here that all top songs which this bot returns are top songs as determined by the number of plays in the United States.

Roadblocks:
- I faced signifcant issues extracting my consumer keys as environment variables. For a while, I experimented with the options for encoding, in an attempt to solve the following error: <<UnicodeEncodeError: 'ascii' codec can't encode character '\u201c' in position 0: ordinal not in range(128).>> However, nothing seemed to work, and I opted to directly copy my consumer keys into my bot's script, replacing them with placeholder strings when uploading to GitHub.
- Additionally, I struggled to deploy my container to EC2. I kept getting the error: <<tweepy.error.TweepError: 'code': 187, 'message': 'Status is a duplicate.'>>, and after failing to get any sort of "try" and "except" conditional to work, I opted to manually delete every mention I had ever sent to my bot's account. This involved asking my family members to delete all mentions from their personal accounts as well. :) This worked, and I was finally able to run my container image in EC2.

## Other K-pop group recommendations from me:

Check out K-pop songs and music videos as the bot informs you! From fashion, to dance, to music, the K-pop genre is ever-expanding, so there is defintely something for everyone to enjoy!

 - Red Velvet
 - NCT 127
 - Stray Kids
 - SHINee
