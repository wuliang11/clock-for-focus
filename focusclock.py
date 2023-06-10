import time

def countdown(T):
    while T > 0:
        mins, secs = divmod(T, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        T -= 1
        
    print("Time's up!")

T = int(input("Enter the countdown time in seconds: "))
countdown(T)
