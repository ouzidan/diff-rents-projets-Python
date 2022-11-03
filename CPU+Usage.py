# importing Python Modules
#psutil
import psutil

CPU = psutil.cpu_count()
print(CPU)
while True:
    Cpu_Percent = psutil.cpu_percent(1)
    print(Cpu_Percent)