class MyClass():
    name = "raghav"
    # name = 'raghav'
    def __init__(self , name, age):
        self.name = name
        self.age = age
    def sum(self , a, b):
        print(a+b)
#
# x = MyClass()
x = MyClass("john" , 20)
print(x.name)
x.sum(4,5)
# del x
del x.name
print(x.age)



