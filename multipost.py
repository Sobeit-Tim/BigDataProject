
precision = 0
recall = 0
for n in range(51, 101):
    file = open("./files/result{}.txt".format(n), "r")
    res = file.read()
    file.close()

    #print("pagerank result, (value, vertex)")
    #print(res)
    res = res.split('\n')

    keywords = []
    for i in res:
        if not i:
            continue
        temp = i.replace(')', ',').split(',')[1]
        keywords.append(temp)

    vocab = {}
    file = open("./files/vocab{}.txt".format(n), "r")
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
    file = open("./new/{}.uncontr.txt".format(n), "r")
    res2 = file.read()
    file.close()
    res2 = res2.split('\n')[0]
    res2 = res2.replace('; ', ' ').split(' ')
    temp = 0
    for i in word_keyword:
        if i in res2:
            temp += 1
    temp = temp/len(word_keyword)
    precision += temp
    temp = 0
    for i in res2:
        if i in word_keyword:
            temp += 1
    temp = temp/len(res2)
    recall += temp

    #print("top n keywords")
    #print(word_keyword)

precision = precision / 50
recall = recall / 50
print("precision ", precision)
print("recall", recall)
