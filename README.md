# topsongs_twitterbot
Tweet a K-pop group's name to @kpop_topsongbot to find out what tracks are trending from your favs!

This bot extracts data from Spotify's Web API to return the Top 3 currently most popular songs by the requested K-pop group. 
How to Use:
Tweet the name of any K-pop group, and tag the twitter handle, @kpop_topsongbot. You can simply tweet the name of the group you are interested in, or you can tweet a complete question which includes that name, such as "What's the latest from Cravity?" or, "What songs are trending by BTS?" My favorite K-pop groups are BTS, DAY6, and Mamamoo, and I would encourage anyone unfamiliar with K-pop to check them out! For K-pop groups with punctuation and spacing in their name, tweet the groupname without those additional characters. For example "NCT 127" becomes "NCT127," and "N'UEST" becomes "NUEST." To access these directions on Twitter, tweet 'help' to the bot. Do not worry about capitalization, the bot will still recognize group names which may be incorrectly capitalized in the user mention. Additionally, this bot only returns song data on still-active K-pop groups. Groups which have disbanded will not be recognized.

How it Works: 
Spotify assigns every song a popularity rating according to the number of plays it as, as well as how recent those plays are. This bot connects to the Spotify Web API to access metadata on the Top 10 most popular songs by the artist specified in the tweet mention. The spotipy library is used to interact with the Spotify API, and the tweepy library is used to interact with the Twitter API. To call the correct Spotify endpoint to access data on the artist's top tracks, this bot's script uses the pandas library to pull the artist ID string of the specified K-pop group from a local csv file mounted to the container running on EC2. I personally compiled this csv, including all the K-pop artists I could think of, so if an existing, still-active, and correctly specified K-pop group is not found by this bot, it is because I have never heard of them. I listen to a wide range of K-pop artists however, and I attempted to compile as comprehensive a list as possible. 
This bot deploys every 30 seconds, so it will take up to 30 seconds for a user's mention to recieve a reply. 

Check out K-pop songs and music videos as the bot informs you! The K-pop genre is ever-expanding, there is defintely something for everyone to enjoy!

Other group recommendations from me:
 - Red Velvet
 - NCT 127
 - BTOB
