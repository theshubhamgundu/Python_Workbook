#it is denoted with{}
#it is a collection  which can store multiple values of different data types
#it is immutable unordered and unindexed
#it cannot store duplicate values
a={12,78,45,12,'abcd',45}
print(a)
for i  in a:
    print(a)
print (12 in a )
#lenght
print(len (a))
b={12,56,78,4,12}
#min,max,sum
print(max(b),min(b),sum(b))
#type()
d=set()
print(d,type(d))
#add
d.add(56)
d.add(34)
print(d)
#update
b.update(d)
print(b)
d.remove(56)
d.discard(99) #no op
d.discard(34)#emp set
print(d)
#pop
print(b.pop())
print(b)
#copy()
e=b.copy()
print(e)
#clear()
b.clear()
print(b)
print(e)
#issubset(),issuperset(),disjoint()
x={1,2,3,4,5,6,7,8,9,0}
y={2,4,6,8}
z={1,3,5,7,9}
print(x.issubset(y),z.issubset(x))
print(x.issuperset(y),z.issuperset(x))
print(y.issubset(y),z.issubset(z))
print(y.isdisjoint(z),x.isdisjoint(y))
#union()
p=y.union(z)
print(p)
a=x.union(z)
print(p)
#intersection()
print(x.intersection(z))
print(y.intersection(z))
print(x.difference(y))
print(y.difference(z))


