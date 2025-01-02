try: 
    a = 10/0
except:
    print("Error handled")
except ValueError as e:
    print(e)