import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("Time's out!")

print("Countdown Timer")
print("---------------")

t = int(input("Enter your desire time in seconds: "))

countdown(t)