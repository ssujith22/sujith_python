import math
principal = 500000
op= 500000
interest_rate = 0.05
mprem = 2684.11
total_paid = 0

while principal >0:
    principal = principal * (1+interest_rate/12) - mprem
    print(total_paid)
    total_paid += mprem

print("total payment for principal: ",op," with interest reate ", interest_rate, "is ",total_paid);
print("total payment for principal: ",op," with interest reate ", interest_rate, "is ",math.ceil(total_paid));
print("total payment for principal: ",op," with interest reate ", interest_rate, "is ",math.floor(total_paid));
print("total payment for principal: ",op," with interest reate ", interest_rate, "is ",round(total_paid,3));

