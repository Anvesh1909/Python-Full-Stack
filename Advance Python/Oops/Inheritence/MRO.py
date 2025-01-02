class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass

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
print("MRO of D Class")
print(D.mro())