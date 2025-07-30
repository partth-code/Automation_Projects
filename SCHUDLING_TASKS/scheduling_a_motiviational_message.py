import time
import schedule
from plyer import notification


def notify(title,message,delay):
    notification.notify(
        title = title,
        message = message,
        timeout = delay
    )
    


if __name__ == "__main__":
    
    #8AM motivation
    schedule.every().day.at("08:00").do(lambda: notify("Motivation","Good Things Ahead 💯",5))
    # schedule.every().second.do(lambda: print("a task"))
    # schedule.every(4).seconds.do(lambda:print("Task in 4 sec"))
    # schedule.every().minute.do(lambda: print("Task every min"))
    # schedule.every(5).minutes.do(lambda:print("Task"))
    # schedule.every().friday.at("5:00").do(lambda: print("Task"))
       
    while True:
        schedule.run_pending()
        time.sleep(1)


    