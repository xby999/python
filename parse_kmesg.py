import sys

vendor = "blue"
venom = "Beginning"
# f_name = "blut.txt"
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
        
        return 10

if __name__ == "__main__":
    print(sys.argv[1])
    print(countInFile(sys.argv[1]))
    
