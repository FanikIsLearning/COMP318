import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt') 

# Activity 1.1
def char_freq(text):
    """
    Function to create a dictionary of character frequencies in the text
    - key is the character
    - value is the frequency (count) of the character in the text
    """
    dFreq = {}
    for char in text:
        if char in dFreq:
            dFreq[char] += 1
        else:
            dFreq[char] = 1
    return dFreq

if __name__ == "__main__":
    import pprint
    s = "At eight o'clock on Thursday morning Arthur didn't feel very good."
    pprint.pprint(char_freq(s))

# Activity 1.2
def word_freq(text):
    # Removing punctuation and making the text lowercase
    text = text
    dFreq = {}
    for word in text.split():
        if word in dFreq:
            dFreq[word] += 1
        else:
            dFreq[word] = 1
    return dFreq

if __name__ == "__main__":
    import pprint

# Activity 1.3
def word_freq(text):
    dFreq = {}
    for word in text.split():  # Iterate over each word in the text
        # Keep the punctuation and case as is
        if word in dFreq:
            dFreq[word] += 1
        else:
            dFreq[word] = 1
    return dFreq

s = """At eight o'clock on Thursday morning Arthur didn't feel very good.  At nine o'clock he strted to feel better."""

import pprint
pprint.pprint(word_freq(s))





    
