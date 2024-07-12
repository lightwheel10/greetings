# python program capable of greeting you with Good Morning, Good Afternoon and Good Evening

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestampint = int(time.strftime('%H'))

print(timestampint)

if (timestampint <= 12):
    print("Good Morning")
elif (timestampint >= 12 and timestampint <= 18):
    print("Good Afternoon") 
elif (timestampint >= 18 and timestampint <= 24):
    print("Good night")


