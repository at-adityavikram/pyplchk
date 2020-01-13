import math
def sentence_split(lines):
    out = []
    for i in range(0,len(lines)):
        lines[i] = lines[i].rstrip("\n")
        for b in lines[i].split("."):
            out.append(b)
    for i in range(0,len(out)-1):
        if out[i] in " ":
            out.remove(out[i])
    return(out)
def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))
def lsum(lst):
    sm = 0 
    for i in lst:
        sm += len(i)
    return sm
chck = input("enter name of file to be checked> ")
source = input("enter name of source file to be checked against> ")
if ".txt" not in chck:
    chck += ".txt"
if ".txt" not in source:
    source += ".txt"
file1=sentence_split(open(chck,"r").readlines())
file2=sentence_split(open(source,"r").readlines())
compare = Diff(file1,file2)
if len(Diff(file1,compare)) != 0:
    print("found " + str(math.ceil((lsum(file1) - lsum(compare))/lsum(file1) * 100.00)) + "% plaigirism at:")
    print(Diff(file1,compare))
else:
    print("original content!")
    
x = input()

