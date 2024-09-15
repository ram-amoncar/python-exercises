from os.path import normpath
from time import sleep
from notifypy import Notify


def drink_water_reminder(interval: int, repeat: int = -1):
    notify = Notify(
        default_notification_title="Stay Hydrated",
        default_notification_application_name="Reminder",
        default_notification_message="Drink Water Now",
        default_notification_icon=normpath("./res/exercise11/water_glass.png"),
    )

    interval_secs = interval * 60

    while True:
        if repeat > 0:
            repeat -= 1
            sleep(interval_secs)
        elif repeat == 0:
            break
        notify.send()


if __name__ == "__main__":
    # reminder every 30 mins
    drink_water_reminder(30)
