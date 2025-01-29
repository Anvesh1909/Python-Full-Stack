
# serialization
d1 = {
    "name" : 'Anvesh',
    "rollno" : 22,
    "fee" : 200.20,
    "Collage" : "SVIT",
    "Present" : True,
    "Backlogs" : None
}

import json
with open("serializ.json","w") as f:
    json.dump(d1,f)
    print("Object serialization is done")
    


# deserialization
import json
with open("serializ.txt","r") as f:
    obj = f.read()
    res = json.loads(obj)
    print(res)
    for k,v in res.items():
        print(k,":",v)
    
    print("Object deserialization is done")
    
