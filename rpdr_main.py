import episodes
import praw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

comments_dict = {
    'comment_id': [],
    'comment' : [],
    'Upvotes_Comment' : [],
    'author' : []
    }
reddit = episodes.reddit

submission = reddit.submission(id=episodes.episodes[-2])
submission.comments.replace_more(limit=None)
for h in submission.comments:
    comments_dict['comment_id'].append(h.id)
    comments_dict['comment'].append(h.body)
    comments_dict['Upvotes_Comment'].append(h.ups)
    comments_dict['author'].append(h.author)


queen_comments = pd.DataFrame(comments_dict)
queens = {'aiden': [], 'sherry': [], 'brita': [], 'heidi': [], 'gigi': [], 'jackie': [], 'widow': [], 'nicky': [], 'crystal': [], 'jaida': [], 'rock m': [], 'dahlia': [], 'jan': []}
queens_copy = queens.copy()
for queen in queens:
    for comment in queen_comments.comment:
        if queen in comment.lower(): 
            queens[queen].append(1)
        else:
            queens[queen].append(0)

queens_only = pd.DataFrame(queens)[['aiden', 'sherry', 'brita', 'heidi', 'gigi', 'jackie', 'widow', 'nicky',
       'crystal', 'jaida', 'rock m', 'dahlia', 'jan']]

# Plot of the most talked about queens
queens_only.sum().sort_values(ascending=False).plot(kind='bar')

# Let's see which queens appeared together
for queen in queens_copy:
    for comment in queen_comments.comment:
        if queen in comment.lower(): 
            queens_copy[queen].append(queen)
        else:
            queens_copy[queen].append(0)
queens_copy = pd.DataFrame(queens_copy)
grouped = []
def groupy(a):
    return list(filter(lambda a: a != 0, a))
for i in queens_copy.iterrows():
        grouped.append(groupy(i[1].to_list()))

queens_copy['grouped'] = [None if len(x)==0 else x for x in grouped]

# we can see which queens are being talked about together
queens_copy['grouped'].apply(lambda x: x if (x is not None and len(x) > 1) else None).value_counts().head(6).plot(kind='bar')
