import sys
import os
import hashlib  

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")  #b binary format

    hobj = hashlib.md5()
    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()  # sum 

def main():
   Ret = CalculateCheckSum("Demo.txt")
   print("Checksum of filr is :",Ret)
if __name__ == "__main__":
    main()
