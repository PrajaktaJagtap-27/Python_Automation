#open function is open also as well create also
def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets opened")
     

        Data = fobj.read(10)
        print(Data)
        fobj.close()
    
    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()