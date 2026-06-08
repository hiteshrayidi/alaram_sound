import time
import winsound
alaram_time=input("Enter alaram time (HH:MM:SS):")
while True:
    current_time=time.strftime("%H:%M:%S")
    if current_time==alaram_time:
        print("Alaram ringing")
        for i in range(5):
            winsound.Beep(1000,500)
        break
    time.sleep(1)