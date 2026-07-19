import schedule
import time
import datetime

def  Display():
    print("Jay Ganesh....",datetime.datetime.now()) 
def main():
    print("Automation script started")   
    
    schedule.every(1).minute.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)         # waiting 1 min and then print jay ganesh  because of the while loop
    print("End of Automation script")
if __name__ =="__main__":
    main()
   