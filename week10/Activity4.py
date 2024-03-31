import nltk
import bs4
import pprint

text = b"Welcome to Python.org Notice: While JavaScript is not essential for this website"
clean_html_text = bs4.BeautifulSoup(text, features="html.parser").getText()

tokens_by_cleaned_split = [token for token in clean_html_text.split()]

pprint.pprint(tokens_by_cleaned_split)
