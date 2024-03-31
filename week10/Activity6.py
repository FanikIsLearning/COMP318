import re
import nltk
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('treebank')

tokens=re.split(' ',"Mark is studying in Centennial College in Toronto")
print(tokens)
tagged=nltk.pos_tag(tokens)
print (tagged)

#Activity 6.2
entities = nltk.chunk.ne_chunk(tagged)
print (entities)

#Activity 6.3
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()