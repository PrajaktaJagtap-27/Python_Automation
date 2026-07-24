#open function is open also as well create also
def main():
    try:
        open("Demo.txt","w") #file create in  auto
        print("file gets opened")
    
    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()