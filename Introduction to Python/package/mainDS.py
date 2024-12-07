from DataStructures.Dict import D1,D2,D3

D = {
    1:"Hello",
    2:"World",
    3:"Welcome to",
    4:"Python programming"
}


print(D1.DictKeys(D))
print(D2.Values(D))
print(D3.items(D))


from DataStructures.List import L1,L2,L3,L3,L4,L5,L6

L = [1,2,3,4,5,5,5]
print(L1.Slicing(L,1,4))
print(L2.index(L,2))
L3.display(L)
print(L4.Add(L,1))
print(L5.Insert(L,2,10))
print(L6.Check(L,10))