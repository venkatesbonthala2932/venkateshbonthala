game_user1=input("choose your class: Warrior, Mage, or Rogue:")
if game_user1=="Warrior":
    weapon="heavy sword"
    health=150
elif game_user1=="Mage":
    weapon="magic staff"
    health=80
elif game_user1=="Rogue":
    weapon="Dual dagger"
    health=100
else:
    print("invalid class selected.Defaulting to peasant")
    weapon="pitchfork"
    health=50
print("you have spawned as a",game_user1,"with a",weapon,"and",health,"HP.")
