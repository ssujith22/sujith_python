wc_teams=["India","Bangladesh","Australia","Pakistan","Newzeland","England"]
wc_wins = [2,0,5,1,0,1]
print(type(wc_teams),wc_teams)
'''
#below query if wc_wins = [2,0,5,1] with out 2 values less compared with wc_teams then we will not get newsland and england
wc_teams=["India","Bangladesh","Australia","Pakistan","Newzeland","England"]
wc_wins = [2,0,5,1]
print(type(wc_teams),wc_teams)

for team,win in zip(wc_teams,wc_wins):
    print(team," won ",win," worldcups ")
''''
wc_teams.sort()
print(wc_teams) #ascending
print(wc_teams[::-1])#descending

print("*" * 40)
for team,win in zip(wc_teams,wc_wins):
    print(team," won ",win," worldcups ")
print("*" * 40)

teams = ":".join(wc_teams) #converting list into a string
print(teams)

wc_teams.append("srilanka")
wc_teams[4] = "Scotland"
print(wc_teams)
wc_teams.insert(2,"West Indies")
print(wc_teams)
wc_teams.extend(["USA","Nepal"])
print(wc_teams)
wc_teams.append(["Srilanka","Nepal"])
print(wc_teams)

print("No of teams participating in WC: ",len(wc_teams))
print("4th team in WC: ",wc_teams[3])
print("last team in WC:", wc_teams[-1])
print("Teams who listed from 3rd to 5th in WC: ",wc_teams[2:5])


i_players = ["Rohit","Virat","Rahul","Hardik"]
a_players = ["Pat","Starc","Warner","Stoinis"]
t_squad = [i_players,a_players]
print(t_squad)
print(t_squad[0][1])
print(t_squad[1][2])
t_squad[0][3] = "Surya";
print(t_squad)

print(wc_teams.pop())
print(wc_teams)
wc_teams.remove("Pakistan")
print(wc_teams)

