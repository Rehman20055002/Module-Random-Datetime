# TAPSIRIQ---------------111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

# 1

# import math
# a=int(input("Kubun terefleri: "))
# print(math.pow( a , 3))

# 2

# a=int(input("Terefi daxil edin"))
# b=int(input("Diger terefi daxil edin"))
# c=int(input("Hundurluyu daxil edin"))
# print("V=",a*b*c)

# 3

# import math
# r=int(input("Radius: "))
# h=int(input("Hundurluk: "))
# print("V=",(math.pi)*(r**2)*(h))


# 4

# import math
# r=int(input("Radius: "))
# h=int(input("Hundurluk: "))
# print("V=",(1/3)*(math.pi)*(r**2)*h)

# 5

# a=int(input("Teref: "))
# h=int(input("Hundurluk: "))
# print("V =",(a**2)*h)

# 6

# import math
# r=int(input("Radius: "))
# print("V=",(4/3)*(math.pi)*(math.pow(r , 3)))




# Tapsiriq-------------------------------------2222222222222222222222222222222222222222222222222222222222222222222222222

# 1

# import math
# try:
#     n=int(input("n:"))
#     r=int(input("r:"))
#     print("C(n,r)=",(math.factorial(n))//((math.factorial(r))*(math.factorial(n-r))))
# except ValueError:
#     print("n , r-den kicik ola bilmez.")


# 2

# import math
# try:
#     n=int(input("n:"))
#     r=int(input("r:"))
#     print("P(n,r)=",(math.factorial(n))//((math.factorial(n-r))))
# except ValueError:
#     print("n , r-den kicik ola bilmez.")




# Tapsiriq-------------------------------------3333333333333333333333333333333333333333333333333333333333333333333333333

# ad=['Elnur','Ramin','Samir','Vaqif']
# import random
# print(random.choices(ad))



# Tapsiriq-------------------------------------444444444444444444444444444444444444444444444444444444444444444444444444444


# import random
# gizli = random.randint(1 , 20)
# say=0

# while True:
#     eded=int(input("1 ile 20 arasinda bir reqem daxil edin: "))
#     say+=1
#     if eded>gizli:
#         print("asagi")
#     elif eded<gizli:
#         print("yuxari")
#     else:
#         print("Dogrudur" , "Texmin" , 5)
#         break

# if say>10:
#     print("Meglub")
# else:
#     print("Qalib")





# Tapsiriq-------------------------------------777777777777777777777777777777777777777777777777777777777777777777777

# from datetime import datetime
# tarix = datetime.strptime("17:00, 04.06.2022", "%H:%M, %d.%m.%Y")
# print(tarix)


# Tapsiriq-------------------------------------8888888888888888888888888888888888888888888888888888888888888888888888

# from datetime import datetime, timedelta
# indi = datetime.now()
# meclis = indi + timedelta(days=7)
# print("Orxan Muellim, sizi", meclis, "tarixinde ciyer axsamina devet edirik")