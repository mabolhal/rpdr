import praw

client_id = 'Q6LswfYdWjvyzA'
client_secret = 'z-g7WIqhWsJkhR6e8xwU5c9PuTs'
user_agent = 'Testing API'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,user_agent=user_agent)

# so let's see if we can automate this process
# # First let's see if we can get the submission id from the title
episodes = []
rpdr = reddit.subreddit('rupaulsdragrace')
for n in range(1,13):
    for i in rpdr.search('UNTUCKED S12E0'+str(n), limit=1):
        if i not in episodes:
            episodes.append(i.id)
