import requests
import bs4
import nltk
import pprint

#Activity 5.1
# Fetch content from a web page, e.g., Python's official site
url = 'https://www.python.org'
response = requests.get(url)
text = response.content

clean_html_text = bs4.BeautifulSoup(text, features="html.parser").getText()
tokens_by_cleaned_split = [token for token in clean_html_text.split()]
# Clean the HTML content
freq_by_nltk=nltk.FreqDist(tokens_by_cleaned_split)
freq_by_nltk

# Print the frequency distribution
pprint.pprint(freq_by_nltk)

#Activity 5.2
import operator   # we need to import this for the following to work
sorted_freq_by_nltk=sorted(freq_by_nltk.items(), key=operator.itemgetter(1), reverse=True)
pprint.pprint(sorted_freq_by_nltk)

#Actvity 5.3
freq_by_nltk.plot(30)  # this plots the first 30 frequencies
freq_by_nltk.plot(30,cumulative=True)