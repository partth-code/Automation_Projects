import schedule
import webbrowser
from win10toast import ToastNotifier
from functools import wraps
import time

def notify(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        
        title = kwargs.pop('title','Notification')
        message= kwargs.pop('message','This is a message')
        span  = kwargs.pop('span',5)
        url = kwargs.pop('url','')
        
        toast = ToastNotifier()
        toast.show_toast(title,message,duration = span)
        
        func(url)
    
    return wrapper

@notify
def open_url(url):
    """This function opens the specified url in webbrowser"""
    webbrowser.open(url)


if __name__ == "__main__":
    
    url = 'https://www.youtube.com/watch?v=utvLy2P6vZ4&list=RDutvLy2P6vZ4&start_radio=1'
    
    #Scheduling the task
    schedule.every().day.at("00:52").do(lambda: open_url(url = url , title = "Song" , message = "Daily Song Reminder" , span = 10))

    
    while True:
        schedule.run_pending()
        time.sleep(1)