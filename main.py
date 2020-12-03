from plyer import notification
import pandas as pd
import time

def notifyMe(title, message, icon_path):
    notification.notify(
        title = title,
        message = message,
        app_icon = icon_path,
        timeout = 10
    )

def Alarm(Reminder_Time):
    return time.strftime("%H:%M:%S", time.localtime()) == str(Reminder_Time)

if __name__ == "__main__":
    excel_file = pd.read_excel('main.xlsx')
    for a, i in enumerate(excel_file['Time']):
        print(i)
        while True:
            if Alarm(i):
                notifyMe(excel_file['Title'][a], excel_file['Message'][a], 'notification.ico')
                break


