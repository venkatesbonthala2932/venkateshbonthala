# a=(5, 10, 15, 20)
# b=(25, 30, 35, 40)
# a,b=b,a
# print("a:",a)   
# print("b:",b)
 

n = int(input (" enter the number of cities you want to enter  : "))
cities=[]
for i in range (n) :
	city=input("enter the name of the city :")
	longitude = float(input(" enter the longitude of the city : "))
	latitude = float( input (" enter the latitude of the city : "))
	
	location = ( longitude , latitude )
	city_1=( city, location)
	cities.append(city_1)

print(cities)
name = input ( " enter the city name you want to search : ")
for i in range (n ):
	if name == cities[i]:
		print (i)
	else:
	 	print(" entered city is not available : " )
