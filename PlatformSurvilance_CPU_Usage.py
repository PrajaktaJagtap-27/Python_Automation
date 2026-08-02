import psutil
import sys
import os
import time
import schedule   

def PlatformSurvillance(FolderName):
    Border = "-"*50

    Ret = False
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not adirectory")
            return
    
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully ") 

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")        

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)   

    fobj = open(FileName,"w") 

    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("------Marvellous Platform Survillance System--------")
    fobj.write("Log file gets created at :"+timestamp+"\n")
    fobj.write(Border+"\n\n")
    
    fobj.write("-------------System Report-----------\n")

    fobj.write(" No of active CPU Cores : %s\n" %psutil.cpu_count()) #add
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())  #Add
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("---------End of log file--------")
    fobj.write(Border+"\n")

    fobj.close()

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
            print("2: It fetch information about the Primary storage as RAM")
            print("3: It fetch information about the secondary storage as HDD")
            print("4: It fetch information about the microprocessor")
            print("5: it gets auto sechudle periodically")
            print("6: it maintain all logs file into log file")
            print("7:its send log file into mail")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "U"):
            print("Use the automation script as :")
            print("python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval :   ")
            print("Folder_Name : name of folder for the log file creation")
        else:
            print("Unable to proceed as there is no matching argument")


        

    #Actual project code    
    elif(len(sys.argv) == 3):
        #print("CPU usage :",psutil.cpu_percent())  #Add 
        print("Schedular started successfully")
        print("Press ctrl+ c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid number of arguments")
        print("Unable to proceed as argument are not matching")
        print("please use --h or --u flag for getting more details")


    
    print(Border)
    print("------Thank you using Automation System------")
    print(Border)


if __name__ == "__main__":
    main()