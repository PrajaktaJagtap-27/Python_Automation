# to run this type python ProcessSurvilance_Process_Log.py > temp.log or simple
#sys.argv[0] is used to get the name of the script which is running and it is used to print the usage of the script
import psutil
import sys
import os
import time
import schedule   

def ProcessScan():  #Add
    listprocess = []

    for proc in psutil.process_iter(): #it is used to get the list of all running process and it returns the list of process object
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None) 
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

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
    
    #CPU information
    fobj.write(" No of active CPU Cores : %s\n" %psutil.cpu_count()) #add
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())  #Add
    fobj.write(Border+"\n")
    
    #RAM information
    memory = psutil.virtual_memory() 

    fobj.write("RAM Usage : %s %%\n" %memory.percent)  #Add
    fobj.write("Toatal RAM Available : %s\n" %memory.total) #Add
    fobj.write(Border+"\n")

    #NEtwork usage

    netobj = psutil.net_io_counters() 
    fobj.write("Network usage report\n")
    fobj.write("sent : %.2f MB" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("receive : %.2f MB" %(netobj.bytes_recv / (1024 * 1024)))

    #ProcessLog   #add
    Data = ProcessScan()

    for info in Data:
        #fobj.write({info}"\n")
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("Name"))
        fobj.write("username : %s\n" %info.get("username"))
        fobj.write("status : %s\n" %info.get("status"))
        fobj.write("usage : %.2f\n" %info.get("cpu_percent"))
        fobj.write("memory : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")

    

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
