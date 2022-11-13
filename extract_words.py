f = open("words.txt", 'r')

words = f.readlines()

f.close()

r = []

for wordb in words:
    word = wordb.strip()
    if len(word) == 5:
        r.append(word)


with open("filtered_words.txt", 'w')as f:
    # for w in r:
    #     f.write(w)
    f.write(str(r))