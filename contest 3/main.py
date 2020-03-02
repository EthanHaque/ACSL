"""
# Third contest of ascl 2019-2020. The veitch program. Takes 4 variables
# and then does the veitch square thing.
# Ethan Haque
# 02/28/2020
"""

def readData(path):
    data = []
    with open(path, "r") as fin:
        for line in fin.readlines():
            data.append(line.strip().split("+")) 
    return(data)

def breakTerm(term):
    brokenTerm, charPos = [], 0
    while charPos < len(term):
        if(term[charPos] != "~"):
            brokenTerm.append(term[charPos])
        else:
            brokenTerm.append(term[charPos] + term[charPos+1])
            charPos += 1
        charPos += 1
    return(brokenTerm)

def vietchSquare(expression):
    coords ={"A":[[0,0], [1,0], [2,0], [3,0], [0,1], [1,1], [2,1], [3,1]],
            "~A":[[0,2], [1,2], [2,2], [3,2], [0,3], [1,3], [2,3], [3,3]],
             "B":[[0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3]],
            "~B":[[2,0], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [3,3]],
             "C":[[0,1], [1,1], [2,1], [3,1], [0,2], [1,2], [2,2], [3,2]],
            "~C":[[0,0], [1,0], [2,0], [3,0], [0,3], [1,3], [2,3], [3,3]],
             "D":[[1,0], [1,1], [1,2], [1,3], [2,0], [2,1], [2,2], [2,3]],
            "~D":[[0,0], [0,1], [0,2], [0,3], [3,0], [3,1], [3,2], [3,3]]}         
    vs = [[False for i in range(4)] for j in range(4)]
    while (len(expression) != 0):
        count = 0  
        term = expression.pop(0)
        square = [[0 for i in range(4)] for j in range(4)]
        for variable in breakTerm(term):
            count += 1
            for coord in coords[variable]:
                square[coord[0]][coord[1]] += 1
        for x in range(len(square)):
            for y in range(len(square[x])):
                if(square[x][y] == count):
                    vs[x][y] = True
    return(vs)

def convertVietchSquareToHex(square):
    out = ""
    for x in square:
        binary = ""
        for y in x:
            if(y == True):
                binary += "1"
            else:
                binary += "0"
        out += hex(int(binary, 2))[-1]
    return(out)

def Main():
    data = readData("data/testData.txt")
    with open("data/fout.txt", "w") as fout:
        for entry in data:
            fout.write(convertVietchSquareToHex(vietchSquare(entry)) + "\n")

Main()
