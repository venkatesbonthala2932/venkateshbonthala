# # #average of numbers in list
list_1=[]
number_elements=int(input("enter the number of elements you want to add in list "))
for i in range(number_elements):
	m=int(input(f"enter the numbers{i+1}: "))
	list_1.append(m)
print(f"the {sum(list_1)} is sum of elements, aveg is {sum(list_1)/number_elements}")

list_1=[]
while True:
	n=input("enter the number or type(stop) if want to stop ")
	if n=="stop":
		break
	list_1.append(int(n))
sum=sum(list_1)
print(sum)
print(list_1)


# #small number and large number in list
lst=[]
while True:
	n = input ( "enter the number or type (stop)after entering : ").lower()
	if n=="stop":
		break
	lst.append(int(n))
lar_num=lst[0]
small_num=lst[0]
for i in lst:
	if i>lar_num:
		lar_num=i
	elif i<small_num:
		small_num=i
print(f"the largest number is {lar_num} and the smallest number is {small_num}")

#reversing a list
reverse_list=list(map(int,input("enter the numbers").split(',')))
print(reverse_list[::-1])
rev=[]
for i in reverse_list:
	rev.insert(0,i)
print(rev)
	


# #removing duplicates from list
lst=list(map(int,input("enter the numbers").split(',')))
result=[]
for i in lst:
	if i not in result: #not is used to check if the element is not already in the result list, if it's not there, it will be added to the result list. This way we ensure that only unique elements are kept in the result list.
		result.append(i)
print(result)



	