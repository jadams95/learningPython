
A = [] # an empty list
B = [123, 'abc', 1.23, {}] #Four items: indexes
C = ['Bob', 40.0, ['dev', 'mgr']] # Nested sublists

"""
C[i]   #Index
C[i][j]#index of index
C[i:j] #Slice
len(C) #Length
"""
C + B # Concat
C * 3 # Repeat

for x in C: print(x) #Concatenate
3 in C # membership

# Methods for growing
C.append(4)
C.extend([5, 6, 7])
print(C)
C.insert(5, 6)
print(C)


# written down as a literal expression a list is coded as a series of objects
# A nested list is coded as a square-bracketed series(row)

#the + operator works the same for lists and strings, 
#it’s important to know that it expects the same sort 
#of sequence on both sides, you get a type error when the code runs
v = str([1, 2]) + "34"
print(v)

#Methods provide type-specific tools; the list methods presented here, 
#for instance, are generally available only for lists.


for x in [1, 2, 3]: #iterating through a list
	print(x, end=' ')
	
	
# modify sort behavior by passing in keyword arguments—a special “name=value”
x = ["AbC", "DEf", "gHi"]
x.sort()
x.sort(key=str.lower)
print(x)
