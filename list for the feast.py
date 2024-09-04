friends= ["Sami","Rija","BD","Shafi","Himel","Magi"]
numbers=[3,6,4,8,10,69]
friends.extend(numbers)
friends[2]= "Borshon"
friends.append("Mashfi")
friends.insert(1,"Kelvin")
friends.remove("Sami")
friends.clear()
friends.pop()
print(friends)
'''print(friends[-1])
here we should remember that, when we are counting 
left to right, that list starts from 0.
but when we are going right to left it start from -1.
print(friends [3:6])'''