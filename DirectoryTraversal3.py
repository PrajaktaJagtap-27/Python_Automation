import os
def main():
    for FolderName , SubFolder, FileName in os.walk("Marvellous"):
        print(FolderName)

        for subf in SubFolder:
            print("SunFolder Name :",subf)

        for fname in FileName:
            print("File name :",fname)

    
if __name__ == "__main__":
    main()
