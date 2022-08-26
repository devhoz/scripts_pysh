import psutil
import os

#To get total CPU

print ('Total CPU:', os.cpu_count())

#to get current CPU usage with 4 sec interval
print ('Current CPU usage is:', psutil.cpu_percent())

#to get total and used memory stat

print ('Memory:', psutil.virtual_memory())
