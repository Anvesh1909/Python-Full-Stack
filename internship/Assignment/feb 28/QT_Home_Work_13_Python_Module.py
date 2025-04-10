# 1
import random

def rand_int():
    res = []

    while len(res)<3:
        a = random.randint(100, 999)
        if a%5==0 and a not in res:
            res.append(a)
    return res

print(rand_int())


# 2
import random

def lottery():
    tickets = random.sample(range(1000000000, 9999999999), 100)
    return random.sample(tickets, 2)

print(lottery())


# 3
import secrets

def otp():
    return secrets.randbelow(900000) + 100000

print(otp())


# 4
import random

def pick_char(s):
    return random.choice(s)

print(pick_char("Anvesh"))


# 5
import random

def rand_string():
    u = [chr(i) for i in range(65,65+26)]
    l = [chr(i) for i in range(97,97+26)]
    return ''.join(random.choices(u+l, k=5))

print(rand_string())

u = [chr(i) for i in range(65,65+26)]
l = [chr(i) for i in range(97,97+26)]
print(u,l)

# 6
import random

def rand_password():
    u = [chr(i) for i in range(65, 65 + 26)]
    l = [chr(i) for i in range(97, 97 + 26)]
    d = [str(i) for i in range(0, 10)] 
    s = ['@', '#', '$', '%', '_', '-', '!', '^']

    password = (
        ''.join(random.choices(u, k=2)) +
        ''.join(random.choices(d, k=1)) +
        ''.join(random.choices(s, k=1)) +
        ''.join(random.choices(u + l + d + s, k=6))
    )
    
    return ''.join(random.sample(password, len(password)))

print(rand_password())



# 7
import random

def multiply():
    num1 = random.uniform(0.1, 1)
    num2 = random.uniform(9.5, 99.5)
    return num1 * num2

print(multiply())


# 8
import secrets

def secure_token():
    return secrets.token_hex(32)

print(secure_token())


# 9
import random

def fixed_dice(n):
    return [random.choice(range(1, 7))] * n

print(fixed_dice(5))


# 10
import random
from datetime import datetime, timedelta

def random_date(start, end):
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    rand_dt = start_dt + timedelta(days=random.randint(0, (end_dt - start_dt).days))
    return rand_dt.strftime("%Y-%m-%d")

print(random_date("2020-01-01", "2025-01-01"))
