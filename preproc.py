from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import getsub


# https://www.youtube.com/watch?v=EvlzEkjVpO8

"""

https://www.youtube.com/watch?v=nKW8Ndu7Mjw
머신 러닝의 7가지 단계 (AI 어드벤쳐)

0:00 | Intro, summary
1:49 | Gathering Data
2:21 | Preparing Data
4:03 | Model Selection
4:30 | Training
6:46 | Evaluation
7:24 | Parameter Tuning
8:55 | Prediction

"""

subtitle = True
step = 1
if subtitle is True:
    step, res = getsub.get()
else:
    file = open("./new/51.abstr", "r")
    res = file.read()
    file.close()

res = res.lower() # lower

# https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
use_tag = ('NN', 'NNS', 'NNPS', 'NNP', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ')

window = int(round(2 * step)) # window size
#print(res)
token_word = word_tokenize(res)
#print(token_word)
tag_word = pos_tag(token_word)
#print(tag_word)
index = 0
vocab = {}
eliminateWord = set(stopwords.words('english'))
eliminateWord2 = set(["'s", ".", ",", "'re", "?", "!", "'ll", "'", "\"", "’", "”", "—", "“", "[", "]"])
for x, i in tag_word:
    if i in use_tag and x not in eliminateWord and x not in eliminateWord2 and x not in vocab:
        vocab[x] = index
        index += 1
print("word - vertex list")
print(vocab)
edge = []
for i in range(len(token_word)):
    if token_word[i] not in vocab:
        continue
    if i+1 == len(token_word):
        break
    endpoint = len(token_word)
    if i+window < endpoint:
        endpoint = i+window
    for j in range(i+1, endpoint):
        if token_word[j] in vocab:
            e1 = (vocab[token_word[i]], vocab[token_word[j]])
            e2 = (vocab[token_word[j]], vocab[token_word[i]])
            if e1 not in edge:
                edge.append(e1)
                edge.append(e2)

edge = sorted(edge)
print("edge list")
print(edge)
file = open("vocab.txt", "w")
for i in vocab:
    file.write("{}\n".format(i))
file.close()

file = open("edges.txt", "w")
for i, j in edge:
    file.write("{} {}\n".format(i, j))
file.close()
