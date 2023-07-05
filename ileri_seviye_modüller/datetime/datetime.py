from datetime import datetime
from datetime import timedelta
"""
simdi = datetime.now()
result = datetime.now()
result = simdi.year
result = datetime.ctime(simdi)
result = datetime.strftime(simdi, "%X")
result = datetime.strftime(simdi, "%Y")
result = datetime.strftime(simdi, "%d")
result = datetime.strftime(simdi, "%A")
result = datetime.strftime(simdi, "%B")
result = datetime.strftime(simdi, "%Y %B %A")
print(result)
"""

""" 
t = "21 Nisan 2019"
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)
"""

"""
t = "21 April 2019 hour 10:12:30"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)
dt = dt.year
print(dt)

birthday = datetime(1983, 5, 9, 12, 30, 10)
print(birthday)
result = datetime.timestamp(birthday) # bulunuştan itibaren geçen süre
print((result))
result = datetime.fromtimestamp(result)
print(result)
result = datetime.fromtimestamp(0) # bilgisayarların bulunuşunu baz alır
print(result)
simdi = datetime.now()
result = simdi - birthday # timedelta
print(result)
# result = result.days
# result = result.seconds
# result = result.microseconds
print(result)

result = simdi + timedelta(days = 10)
print(result)
"""