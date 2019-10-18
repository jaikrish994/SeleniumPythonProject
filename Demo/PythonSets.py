my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)
print("Chalk" in my_set)
my_set.add("Pen")
print(my_set)
my_set.update(["Pencil", "Eraser"])
print(my_set)
print(len(my_set))
my_set.remove("Pencil")
print(my_set)
my_set.discard("Pen")
print(my_set)
my_set.pop()
my_set.clear()
print(my_set)
del my_set

my_set_1 = ["Apples", 1,2,3, {"Mango", "Apple", "Banana"}]
print(my_set_1)

my_set_2 = {"Apples", 1,2, (3,4,5)}
print(my_set_2)
my_list = [1,2,3]
print(my_list)
my_set_3 = set(my_list)
print(my_set_3)
A = {"A", "B", 1, 2, 3}
B = {"B", "C", 3, 4, 5}
print(A.union(B))
print(A | B)
print(A.intersection(B))
print(A & B)
print(A.difference(B))
print(A-B)
print(A.symmetric_difference(B))
print(A^B)

