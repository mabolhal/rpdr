import praw

client_id = '-'
client_secret = '-'
user_agent = '-'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,user_agent=user_agent)

episodes = []
rpdr = reddit.subreddit('rupaulsdragrace')
for n in range(1,13):
    for i in rpdr.search('UNTUCKED S12E0'+str(n), limit=1):
        if i not in episodes:
            episodes.append(i.id)
