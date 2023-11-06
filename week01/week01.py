# Activity 1#
import this

print("-------------------------------------------")

# Activity 1 - Math Functions#
a = 1 + 1
print(a)
import math

print(math.sin(1))
print(math.sin(90))
print(math.pi)
print(math.sin((math.pi / 2)))
print(math.sin(0))
print(math.cos(0))
print(math.cos(math.pi))
sinpi = math.sin((math.pi / 2))
print(sinpi)
print("*****************")
# Todo : Create List and display their elements
lst = [1, 2, 3, 4, 5]
print(lst)
print(lst[:3])
print(lst[2:3])
print(lst[2:-1])
print(lst[-1])
print(lst[-3])
print(lst[:-3])
lst1 = [6, 7, 8, 9, 10]
newlst = lst + lst1
print(newlst)
lst.append(3)
print(lst)
# help(newlst)
lst1.insert(0, 4)
print(lst1)
lst1.insert(0, 5)
print(lst1)
newlst = lst + lst1
print(newlst)
print(newlst.sort)
newlst.sort()
print(newlst)
newlst.reverse()
print(newlst)

print("-------------------------------------------")
# Activity 2 - Create and display dictionary#
d = {}
d["one"] = 1
d["two"] = 2
print(d)
print(len(d))
print(d.keys())
print(d.values())
import pprint

pprint.pprint(d)
pprint.pprint(newlst)
d["complex"] = {}
pprint.pprint(d)
d["complex"]["yellow"] = [255, 255, 0]
pprint.pprint(d)
# help(pprint)
d["complex"]["red"] = [255, 0, 0]
d["complex"]["green"] = [0, 255, 0]
d["complex"]["blue"] = [0, 0, 255]
pprint.pprint(d)
print(d)
print("-------------------------------------------")


# Activity 3 - Define functions and run them#
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
print("\n", fact(100))
print("\n", fact(200))
print("-------------------------------------------")
# Activity Todo#
from fibonacci import fibonacci

result = fibonacci(10)
print(result)
