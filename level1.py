# top_scores=[8500,9200,7800,9900,8100]
# new_player=int(input("enter your score :"))
# top_scores.append(new_player)
# top_scores.sort(reverse=True)
# print(f"the absolute highest score {top_scores[0]}")


# temp_weights=[]
# for i in range(3):
# 	m=float(input(f"enter three decimal numbers {i+1}: "))
# 	temp_weights.append(m)

# locked_ai_weights=tuple(temp_weights)
# total=locked_ai_weights[0]+locked_ai_weights[1]+locked_ai_weights[2]
# print(f"{locked_ai_weights} and the total is {total}")

player_bag = ["Sword", "Trash", "Shield", "Trash", "Health Potion", "Trash"]
clean_bag = []
print("len(player_bag):", len(player_bag))
for i in range(len(player_bag)):
	if player_bag[i]!="Trash":
		temp=player_bag[i]
		clean_bag.append(temp)
		print("clean_bag:", clean_bag)
		i=i+1
	else:
		print("no")
		i+1
print("clean bag:", clean_bag)

# player_bag = ["Sword", "Trash", "Shield", "Trash", "Health Potion", "Trash"]
# clean_bag = []
# for item in player_bag:
#     if item != "Trash":
#         clean_bag.append(item)
#         print(f"kept {item} in clean_bag: {clean_bag}")                
#     else:
#         print("discarded Trash")
# print("final clean_bag:", clean_bag)
