import sys

vendor = "blue"
venom = "Beginning"
f_name = "blut.txt"
#count = 0
def countInFile(filename):
    aa = 0

    with open(filename,'r+t',encoding='utf-8') as f:
        contents = f.readlines()
        for line in contents:
            str = line
            if str.find(vendor) != -1:
                aa+=1
                print(aa)
            if str.find(venom) != -1:
                aa-=1
                print(aa)  
        print(contents[-1])
        str1 = contents[-1]
        print(str1.split("tuple")[1])
        return 10

if __name__ == "__main__":
    #print(sys.argv[1])
    print(countInFile(f_name))
