# typecasting is the process of converting a variable from one data type to another data type.
#(string, integer, float, boolean)
#Explicit vs Implicit typecasting

name  = "bro"
age = 21
gpa = 1.9
student = True

#Explicit typecasting
age = int(age)
gpa = str(gpa)

print(type(age), type(gpa))



#Implicit typecasting
x = 2
y = 2.0
x = x / y

print(x)