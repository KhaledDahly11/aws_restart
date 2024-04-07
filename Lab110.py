myString = "This is a string."
print (myString)
print(type(myString))
print (str(myString) + " is of the data type " + str(type(myString)))

firstString="water"
secondString="fall"
thirdString=firstString + secondString
print (thirdString)

name=input("What is your name? ")
print (name)

color = input("What is favorite color? ")
animal = input("What is favorite animal? ")
print ("{}, you like a {} {}!".format(name,color,animal))