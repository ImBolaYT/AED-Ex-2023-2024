# Translate an x amount of seconds into the Hours, Minutes, Seconds

total = int(input("Indique o tempo em segundos:"))

hours= int(total/3600)  
total-= hours*3600      

minutes = int(total/60)  
total -=  minutes*60       

print("{0} horas, {1} minutos, {2} segundos".format(hours, minutes, total) )