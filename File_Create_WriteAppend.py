#open function is open also as well create also
def main():
    try:
        fobj=open("Demo.txt","a")
        print("file gets opened")
        fobj.write("Marvellous infosystems")

        fobj.close()
    
    except FileNotFoundError as fobj:
        print("File is not present in current directory")


if __name__ == "__main__":
    main()