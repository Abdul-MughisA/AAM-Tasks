#This program outputs time in seconds.
time = input("Enter the time (e.g.: HH:MM::SS): ")
time = time.replace(":"," ")
time = time.split()
for i in range(0,3):
    time[i] = int(time[i])
#end for
hours = time[0] * 60 * 60
minutes = time[1] * 60
seconds = time[2]
total = hours + minutes + seconds
print("Your total is", total, "seconds.")