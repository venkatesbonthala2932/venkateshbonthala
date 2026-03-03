palindrome_1 = []
m = int(input("Enter how many elements: "))

for i in range(m):
    n = str(input(f"Enter element {i+1}: "))
    palindrome_1.append(n)

palindrome_2 = palindrome_1[::-1] 
  
print("Original:", palindrome_1)
print("Reversed:", palindrome_2)

if palindrome_1 == palindrome_2:
    print("It is a palindrome")
else:
    print(" It is NOT a palindrome")