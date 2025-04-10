
# 10
import random
from datetime import datetime, timedelta

def random_date(start, end):
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    rand_dt = start_dt + timedelta(days=random.randint(0, (end_dt - start_dt).days))
    return rand_dt.strftime("%Y-%m-%d")

print(random_date("2020-01-01", "2025-01-01"))
