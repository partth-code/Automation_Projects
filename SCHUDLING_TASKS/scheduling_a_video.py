import schedule
import time
from plyer import notification
import webbrowser
from functools import wraps




def notify(func):
    @wraps(func)
    def wrapper(*args , **kwargs):
        
        title = kwargs.pop('title','Notification')
        message = kwargs.pop('message',"This is a message")
        span = kwargs.pop('span',5)
        url = kwargs.pop('url','')
        
        notification.notify(
            title = title,
            message = message,
            timeout = span
        )
        func(url)

    return wrapper


@notify
def open_site(url):
    webbrowser.open(url)


if __name__ == "__main__":
    
    url = 'https://www.youtube.com/watch?v=utvLy2P6vZ4&list=RDutvLy2P6vZ4&start_radio=1'
    
    schedule.every().day.at("00:33").do(lambda: open_site(url= url , title = 'Opening Site' , message = 'Daily Song Reminder' , span = 5 ))
    
    while True:
        schedule.run_pending()
        time.sleep(1)