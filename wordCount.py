import matplotlib.pyplot as plt
import re

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


f = open("book.txt", 'r', encoding='utf-8')
wordList = list(f.read())
wordCount = {}
totalWords = 0
for word in wordList:
    if re.match('\\w', word):
        totalWords += 1
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
# max 9
maxList = []
maxCount = []
nowPercentage = 0
expectedPercentage = 0.99
while nowPercentage < expectedPercentage:
    maxCount.append(0)
    maxList.append("")
    for word, count in wordCount.items():
        if maxCount[-1] < count:
            maxCount[-1] = count
            maxList[-1] = word
    wordCount.pop(maxList[-1])
    nowPercentage = 0
    for val in maxCount:
        nowPercentage += val / totalWords
print(maxList, [val / totalWords for val in maxCount], sep="\n")
maxList.append("其它")
maxCount.append(int((1-nowPercentage) * totalWords))

fig = plt.figure(figsize=(32, 32))
ax1 = fig.add_subplot(111)
# plt.title('Harry Potter Words Count')
tupleBuilder = [0.0 for index in range(len(maxCount))]
tupleBuilder[0] = 0.1
explode = tuple(tupleBuilder)
ax1.pie(maxCount, labels=maxList, autopct='%1.1f%%', explode=explode, textprops={'size': 'xx-large'})
ax1.axis('equal')
ax1.set_title('Harry Potter Words Count')
plt.savefig('statistic.png')
plt.show()
