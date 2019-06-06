import time
import webbrowser

total_breaks =  100
break_count = 0

print ("Program has started on" + time.ctime())

while(break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("--app=https://www.youtube.com/watch?v=M1wLtAXDgqg")
    break_count =+ break_count