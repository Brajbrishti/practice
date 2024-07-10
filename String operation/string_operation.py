x={}

print("How many players")
n=int(input())

for i in range(n):
    print("Enter player name :",end='')
    pname=input()
    print("Enter his score :",end='')
    score=int(input())
    x.update({pname:score})
print(x)
print("+++++++++++++++++++++++++++++++++++++++")

print("Players are  in this match :")
for pname in x.keys():
    print(pname )
print("Enter player name :",end='')
name=input()
runs=x.get(name,-1) ###
if (runs == -1):
    print("player is not listed")
else:
    print("{} made runs {}.".format(name,runs))