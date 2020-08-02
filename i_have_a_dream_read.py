with open("i_have_a_dream.txt", "r") as my_file:
    i=0
    while 1:
        line=my_file.readline().replace("\n","")
        if line.strip()=="":
            continue
        if not line:
            break
        print(str(i)+"==="+line)
        i=i+1
