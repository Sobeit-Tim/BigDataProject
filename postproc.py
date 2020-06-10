
file = open("result.txt", "r")
res = file.read()
file.close()

print("pagerank result, (value, vertex)")
print(res)
res = res.split('\n')

keywords = []
for i in res:
    if not i:
        continue
    temp = i.replace(')', ',').split(',')[1]
    keywords.append(temp)

vocab = {}
file = open("vocab.txt", "r")
res2 = file.read()
file.close()

res2 = res2.split('\n')

cnt = 0
for i in res2:
    if not i:
        continue
    vocab[cnt] = i
    cnt += 1
word_keyword = []
for i in keywords:
    word_keyword.append(vocab[int(i)])
print("top 3 keywords")
print(word_keyword)
