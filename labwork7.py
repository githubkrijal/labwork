#you live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. how long will bus journey take? Alternatively, you could run to university
#you jog the first mile at 7mph; then run the next two at 15mph; beforejogging the last at 7mph again.
#will thi be te quicker orr slower than the bus?

distance=4*1.609*1000
bus_speed=25
timetaken=((distance/bus_speed)*60)
timespends=20
totaltime=timetaken=timespends
print("total time taken by bus is",totaltime)

jog1=((1/7)*60)
jog2=((2/15)*60)
jog3=((1/7)*60)
totaljogtime=jog1+jog2+jog3
print("the jogging time is",totaljogtime)

if(totaltime > totaljogtime):
    print("Taking bus is slower")
else:
    print("Taking bus is quicker")