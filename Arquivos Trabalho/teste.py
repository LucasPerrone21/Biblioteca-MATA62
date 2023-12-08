from datetime import date, timedelta

x = date.today()

print(type(x))
print(type(x.strftime("%d/%m/%Y")))