lst=list(map(str,input("enter to find the longest word : ").split(',')))
i=0
j=0
for i in range(len(lst)):
	if len(lst[i])>j:
		j=len(lst[i])
		if j==len(lst[i]):
                 longest_word=lst[i]
print(j)
print(longest_word) 