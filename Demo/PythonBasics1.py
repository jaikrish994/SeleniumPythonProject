print("hello world")
x = 5
y = "Automation"
print(x)
print(y)
print("Hello" +y)
print ("Result" +str(x))
x = 10
y = 20
print(x+y)

if 10>5:
    print("10 is greater than 5")
def sum(a, b):
    print(a+b)
x = sum(10, 5)

x = 5
y = 2.5
z= 4j
print(type(x))
print(type(y))
print(type(z))
# casting
x = int(2)
y = int(2.5)
z = float(1)
p = str(10)

print(x)
print(y)
print(z)
print(int(p)+x)

x = "Hello World.."
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())

x = "  Hello World... "
print(x)
print(x.strip())
print(x.replace("e","a"))
x = " Hello , World"
print(x.split(","))

print("Enter your name:")
x= input()
print("hello," +x)