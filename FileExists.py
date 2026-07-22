import os

def main():
   
   if(os.path.exists("Demo.txt")):  #update
     print("Fils is present in current directory")
   else:
    print("there is such no file")

    


if __name__ == "__main__":
    main()
