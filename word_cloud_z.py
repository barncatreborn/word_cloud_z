##https://www.geeksforgeeks.org/generating-word-cloud-python/

# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import re

str_path_csv_z = "barncatreborn.csv"
# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv(str_path_csv_z, encoding ="latin-1")

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df["each_tweet_text_z"]:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		this_word_raw_z = tokens[i].lower()
		if re.fullmatch(r'\A[a-z]{6}\Z', this_word_raw_z) is not None:
			tokens[i] = this_word_raw_z
		else:
			tokens[i] = ""
	
	comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
print("ok")