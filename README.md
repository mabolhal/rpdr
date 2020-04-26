# Rupaul's Drag Race - Untucked!
Simple plots based on Reddit comments for "RuPaul's Drag Race: Untucked!" + Sentiment Analysis using Classification

# Summary
Each week, my friends and I watch RuPaul's Drag Race (given the circumstances we do so virtually ensemble).
Each episode contains challenges where queens compete for the grand prize of $100,000; this is followed by Untucked! where the queens go backstage to have a drink and banter. Sometimes the banter can get heated. This project is to detail the drama in the plots, and expose RPDR fans' sentiment via simple visualizations.

The main file is "May the Best Woman Win!.ipynb" notebook. Here, we use a machine learning model to perform sentiment analysis on the reddit comments for each of the Untucked! episodes. The model classifies comments to either 1 or 0 (Positive/Negative respectively), and was built using Logistic Regression. Additionally the model was trained using imdb movie reviews - labelled data I could find that most closely resembles the comments. 

I have retrieved the comments via Reddit's praw library. The file "episodes.py" is used to init the praw class. 

# Enjoy!
And feel free to provide feedback. 

https://www.linkedin.com/in/mabolhal
