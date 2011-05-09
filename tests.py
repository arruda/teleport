from divide_by_zero.worm_holes import worm_hole

me = "Felipe Arruda Pontes"
my_home = 123127248120219432812
her_home = 12873012024791234841
my_will = 99999999999999999999

from datetime import datetime
time = datetime.now()


hole = worm_hole(my_home,her_home,time,time)



hole.create(my_will,True)

hole.transport(me)
