# sets 
# O(1)

st1 = {2, 5, 7, 4}
st2 = {2, 3, 5, 6}
st3 = {2, 3, 4, 5, 6, 7}
st4 = {4, 5}

# O(1)
st1.add(9)
st1.remove(9)

a = st1.intersection(st2)
i = st1 | st2
b = st1.union(st2)
h = st1 & st2

# bool
c = st1.issubset(st3)
d = st1.issuperset(st4)

e = st1.difference(st2)
f = st2.difference(st1)

g = st1.symmetric_difference(st2)

print (a,b,c,d,e,f, g)


# to create copy of set (Shallow Copy)
# st5 = st4[:] 
st5 = st4.copy()

st6 = {}
print(type(st6))
st7 = set()
print(type(st7))

#we can add multiple element using update
st1.update([8,9])
#discard won't show error if 8 does not exist
sr1.discard(8)

#concatenation
print("_".join(st1)) 