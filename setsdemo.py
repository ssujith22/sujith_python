luck_draws = set()
print(type(luck_draws),luck_draws)

luck_draws_o = {14,18,35,37,67,55,40,18,37}
luck_draws_s = {11,18,35,36,66,55,43}
luck_draws_s.add(4)
luck_draws_s.discard(43)

print("online draws",luck_draws_o,len(luck_draws_o))
print("shop draws",luck_draws_s)

print("*" * 40)
for draw in luck_draws_o:
    print(draw)

print("*" * 40)
print("union ",luck_draws_o | luck_draws_s)
print("intersect",luck_draws_o & luck_draws_s)
print("different between online - shopping", luck_draws_o - luck_draws_s)
print("different betwen shopping - online",luck_draws_s - luck_draws_o)

set1 = {1,3,5}
set2 = {5,1,3}
print(set1 ==set2) #returns true irrespective of its position in the set if both sets are having
