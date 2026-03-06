lst=list(map(int,input("enter the numbers : ").split(',')))
k=int(input("enter the number of times you want to rotate : "))
n=len(lst)
k=k%n
first_lst=lst[-k:]
last_lst=lst[:-k]
print(first_lst+last_lst)