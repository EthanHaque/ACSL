with open("sameness.in", "r") as fin, open("sameness.out", "w") as fout:
    for line in fin.readlines():
        word1, word2, = line.split(" ")[0].strip(), line.split(" ")[1].strip()
        count, total = 0, 0
        while count < len(word1) and count < len(word2):
            if word1[count] == word2[count]:
                word1, word2 = (word1[:count] + word1[count+1:]), (word2[:count] + word2[count+1:])
            else:
                count += 1
        count = 0  
        while count < len(word1) and count < len(word2):
            if(word1[count] == word2[count]):
                word1, word2 = (word1[:count] + word1[count+1:]), (word2[:count] + word2[count+1:])
            elif(count + 2 > len(word2)):
                break
            elif(word1[count] == word2[count+1]):
                word2 = word2[:count] + word2[count+1:]
            elif(count + 2 > len(word1)):
                break
            elif(word2[count] == word1[count+1]):
                word1 = word1[:count] + word1[count+1:]
            else:
                count +=1
        for letter1, letter2 in zip(word1, word2):
            total += ord(letter1) - ord(letter2)
        total += abs(len(word1) - len(word2))
        print(total)