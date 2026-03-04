#to find the second largest number in a list

lst=list(map(int, input("enter the numbers : ").split(',')))
ref=[]
for i in lst:
    if i not in ref:
        ref.append(i)
if len(ref)<2:
	print("there will be no second largest")
larg=-float('inf')
sec_larg=-float('inf')
for i in ref:
	if i>larg:
		sec_larg=larg
		larg=i
	if i!=larg and i>sec_larg:
		sec_larg=i
print (sec_larg)


	
	

		