marks=[]
for i in range(5):
	
	m=int(input((f"enter marks {i+1}:")))
	marks.append(m)
print("total marks:", marks)
print("sum of all the marks :", sum(marks))
print("average of all the marks :", sum(marks)/len(marks))
print(marks.reverse())
print(marks)

