blood_red1=[]
for i in range(3):
	m=int(input(f"set the blood red RGB:"))
	i+=1
	blood_red1.append(m)
blood_red=tuple(blood_red1)
print("blood red RGB:", blood_red)
print(type(blood_red) )

dark_black1=[]
for i in range(3):
	m=int(input(f"set the dark black RGB:"))
	i+=1
	dark_black1.append(m)
dark_black=tuple(dark_black1)
print("dark black RGB:", dark_black)
print(f"{dark_black.count(dark_black[0])} times the same number {(dark_black[0])} is repeated in darkblack ")
print(type(dark_black) )
