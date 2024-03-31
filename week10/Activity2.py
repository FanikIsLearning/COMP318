# Activity 2.1 : Run each step in IDLE and display the results
import urllib.request as req   # the request object
# Optional: run dir(req) to see the properties and methods of urllib.request module
resp=req.urlopen("https://www.python.org")   # response object
text=resp.read()                             # read the web page 
# Optional: text1=resp.read(100)              # read the 100 elements of the web page
print(text)                               

""" Output:
b'<!doctype html>\n<!--[if lt IE 7]>
... 
"""

# Note the 'b' in the output above. It indicates that text is in a binary format

# Activity 2.2
# tokenize by using python string's split method:

tokens_by_split=text.split()

import pprint
#pprint.pprint(tokens_by_split)      # this outputs everything, which could be quite big

pprint.pprint(tokens_by_split[:100]) # this outputs only up to the first 100 items   

"""
Output:
[b'<!doctype',
 b'html>',
 b'<!--[if',
 b'lt',
 b'IE',
 b'7]>',
 b'<html',
 b'class="no-js',
 b'ie6',
 b'lt-ie7',

...
"""