# Python Projects: Countdown Timer 🐍
Python Script <br>
This repo contains python code that generates a timer. <br>
Run the code.

Python
```python
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


    print('Timer completed!')

t = input('Enter the time in seconds: ')

countdown(int(t))
```

Output
```python
00:60
Timer completed!
```
