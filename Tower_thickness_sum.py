
"""one morning you go out and place a dollar bill on the sidewalk by the ust tower in trivendrum.
each day thereafter you out double the number of bills, How long does it take for the stack of bills to exceed the tower,
if the tower height is 442 and thickness of bill is 0.11m"""

import math
tower_height = 442
thicknes_of_bill = 0.11
no_of_bills = 1
days = 1
while(no_of_bills *thicknes_of_bill <tower_height):
    days+=1
    no_of_bills *=2
    
print ("no of days to reach tower height - ",days)
print ("no of days to reach tower height - ",no_of_bills)
print ("no of days to reach tower height - ",no_of_bills *thicknes_of_bill)


