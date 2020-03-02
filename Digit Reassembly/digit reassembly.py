"""
ID: ehaque2
LANG: PYTHON3
TASK: DIGIT REASSEMBLY
"""

fin = open("digit reassembly.in", "r")
fout = open("digit reassembly.out", "w")
contents = fin.read().split("\n")
contents = [i.split(" ") for i in contents]
count = 0
summation = 0
for i in contents:
    seq = i[0]
    length = int(i[1])
    if(len(seq)%length != 0):
        for i in range(length - len(seq)%length):
            seq = seq + "0"
    for i in range((len(seq) // length)):
        summation += int(seq[((i*length)):(length*(i+1))])
    fout.write((str(count) + ". " + str(summation) + "\n"))
    count += 1
    summation = 0
fout.close()