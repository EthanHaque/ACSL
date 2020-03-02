with open("transform.in", "r") as fin, open("transform.out", "w") as fout:
    for count, line in enumerate(fin.readlines(), 1):
        N, Np = line.split(" ")[0], line.split(" ")[0][len(line.split(" ")[0]) - int(line.split(" ")[1])]
        fout.write(str(count) + ". ")
        for position, character in enumerate(N, 0):
            fout.write(str((int(N[position]) + int(Np))%10) if position < (len(N)-int(line.split(" ")[1])) else Np + "\n" if (line.split(" ")[1].strip() == "1") else Np if position == (len(N)-int(line.split(" ")[1])) else str(abs(int(N[position]) - int(Np)%10)) if position < len(N)-1 else (str(abs(int(N[position]) - int(Np)%10)) + "\n"))
 
