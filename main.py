import time
from plyer import notification

while True:
    print("Time to drink water!")
    notification.notify(
        title="Drink Water Reminder",
        message="It's time to drink water and stay hydrated!",
        app_name="Drink Water Reminders",
        timeout=10  # Notification will be visible for 10 seconds
    )
    time.sleep(3600)