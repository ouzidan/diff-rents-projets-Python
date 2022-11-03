# import Python Modules
# time
# psutil
# plyer
import time
import psutil
from plyer import notification

battery = psutil.sensors_battery()
percent = battery.percent

notification.notify(
    title="Battery Percentage",
    message=str(percent) + "% Battery Remaining",
    timeout=20
)

