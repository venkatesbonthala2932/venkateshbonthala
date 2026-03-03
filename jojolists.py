jostar_team=[]
number_members=int(input("enter the number of members you want to add in jostar team "))
for i in range(number_members):
	m = str(input(f"add your member {i+1}:")).lower()
	jostar_team.append(m)
print("jostar members:",jostar_team)
if "jonathan" in jostar_team:
    jostar_team.remove("jonathan")
    jostar_team.append("kakyoin")
    print("after removing jonathan from jostar team:",jostar_team)
else:
    print("the final trip for the team:",jostar_team )