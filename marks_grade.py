m = int(input("Enter maths marks: "))
s = int(input("Enter science marks: ")) 
e = int(input("Enter english marks: "))
total = m+s+e 
average = total/3 
print(total) 
print(average) 
if average > 90:
     print("A")
     elif average >75 and average <= 90: 
     print("B")
     elif average > 50 and average <=75:
     print("C")
else:
     print("Fail")