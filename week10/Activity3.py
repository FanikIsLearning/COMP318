import re
# text comes from previous activity, however it is a binary array; we need to convert it to string
text = b"At eight o'clock on Thursday morning Arthur didn't feel very good."
text=str(text,'utf8')             # now this should work 
tokens_by_re=re.split(r'\W+', text)  # split on regular expression r'\W+' (r stands for 'raw')

print("len(tokens_by_re)")  #
print(len(tokens_by_re))  #
print("Up to 100 tokens from tokens_from_re")
print(tokens_by_re[:100]) # print the first 100 tokens (if there are >100), or all tokens (if <=100)

import pprint
pprint.pprint(tokens_by_re[:100])  # pretty-printing up to 100 items 