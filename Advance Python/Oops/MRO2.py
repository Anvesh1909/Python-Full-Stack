class A: pass
class B: pass
class C: pass
class X(A,B): pass
class Y(B,C): pass
class Z(X,Y,C): pass

print()
print("MRO of A Class")
print(A.mro())

print()
print("MRO of B Class")
print(B.mro())

print()
print("MRO of C Class")
print(C.mro())

print()
print("MRO of X Class")
print(X.mro())

print()
print("MRO of Y Class")
print(Y.mro())

print()
print("MRO of Z Class")
print(Z.mro())