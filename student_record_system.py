student_record = []
number_students = int(input(" enter the number of student's you want to enter int the register : "))
if number_students == 0 :
	print (" you have to enter the student's number ")
for i in range ( number_students ) :
	student_id=int(input(" enter the  student number : "))
	name= input(" enter the name of the student : ")
	age= input(" enter the age of the student : ")

	b=(student_id,name,age)
	student_record.append(b)
print(student_record)
name = input ( " enter the name of the student you want to search : ")
age_1=0

for i in range(len(student_record)):
	i+2
	if age_1 > (student_record[i]) :
		oldest=age_1
	else:
		age_1=student_record[i]

for i in  range(len(student_record)) :
	if name in student_record[i]:
		print(student_record[i])	

	 
		
