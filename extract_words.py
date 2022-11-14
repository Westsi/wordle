f = open("words.txt", 'r')

words = f.readlines()

f.close()

r = []

for wordb in words:
    word = wordb.strip()
    if len(word) == 5:
        r.append(word)


with open("filtered_words.txt", 'w')as f:
    f.write('[\n')
    for w in r:
        f.write('\t"' + w + '",\n')
    f.write(']')