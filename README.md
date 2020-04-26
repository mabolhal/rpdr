# Rupaul's Drag Race - Untucked!
Simple plots based on Reddit comments for "Untucked!"

# Quick Rundown 
Each week, my friends and I watch RuPaul's Drag Race (obviously in current times, we ZOOM).
Each episode is followed by Untucked! where the queens go backstage to have a drink and banter. 
Sometimes the banter can get heated. 

The main file is "May the Best Woman Win!.ipynb" notebook. Here, we use a trained machine learning model to perform sentiment analysis on the reddit comments for each of the Untucked! episodes. The model classifies comments either to 1 or 0 (Positive/Negative respectively). The model was built using Logistic Regression and is trained using imdb movie reviews - labelled data I could find that most closely resembles the comments. 

I have retrieved the comments via Reddit's praw library on Python. The file "episodes.py" is used to init the praw class. 

# Enjoy!
And feel free to provide feedback. 

LinkedIn
linkedin.com/in/mabolhal

