with open("sameness.in", "r") as fin, open("sameness.out", "w") as fout:
    for line in fin.readlines():
        word1, word2, = map(str, line.split(" "))
        while len(word1) > 0 and len(word2) > 0: 
            if(word1[0] == word2[0]):
                word1, word2 = word1[1:], word2[1:]
            elif(word1[0] == word2[1]):
                word1, word2 = word1[1:], word2[2:]
            elif(word2[0] == word1[1]):
                word2, word1 = word2[1:], word1[2:]
            else:
                break
        total = 0
        if len(word1) >= len(word2):
            for i in range(len(word2)):
                total += ord(word1[i]) - ord(word2[i])
            total += len(word1) - len(word2)
        else:
            for i in range(len(word1)):
                total += ord(word1[i]) - ord(word2[i])
            total += len(word2) - len(word1)
        print(total)

