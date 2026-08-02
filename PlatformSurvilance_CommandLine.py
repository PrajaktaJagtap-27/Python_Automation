# to run this python ProcessSurvillance.py 2 MarvellousLog
# python ProcessSurvillance.py Time interval Folder_Name
# len(sys.argv) -->3

#python ProcessSurvillance.py --h
# python ProcessSurvillance.py --u

import psutil
import sys
import os

def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Survillance System--------")
    print(Border)
 
    #--h and --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "H"):
            print("This automation script is use to perform")
            print("1: It fetch the information of running proceess")
            print("2: it fetch information about the Primary storage as RAM")
            print("3: it fetch information about the secondary storage as HDD")
            print("4: it fetch information about the microprocessor")
            print("5: it gets auto sechudle periodically")
            print("6: it maintain all logs file into log file")
            print("7:its send log file into mail")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "U"):
            print("Use the automation script as :")
            print("python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval :  ")
            print("Folder_Name : name of folder for the log file creation")
        else:
            print("Unable to proceed as there is no matching argument")


        

    #actual project code
    elif(len(sys.argv) == 3):
        pass
    
    else:
        print("Invalid number of arguments")
        print("Unable to proceed as argument are not matching")
        print("please use --h or --u flag for getting more details")


    
    print(Border)
    print("Thank you using Automation System")
    print(Border)


if __name__ == "__main__":
    main()