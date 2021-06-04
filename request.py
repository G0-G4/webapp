import requests, datetime, random
from time import sleep

# d = {
#     'device_id' : 3,
#     'x' : 3.5,
#     'y' : 5.4,
#     'tempreture': 36.3,
#     'date': datetime.datetime.today()
# }

for i in range(100):
    d = {
    'device_id' : random.randint(1,5),
    'x' : random.uniform(0, 10),
    'y' : random.uniform(0, 10),
    'tempreture': random.uniform(15, 30),
    'date': datetime.datetime.today()}
    r = requests.post('http://127.0.0.1:5000/post' , data = d)
    sleep(0.5)

print('success')