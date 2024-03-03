# bounce.py
#
# Exercise 1.5
bounces=0
height=100

while bounces <10:
    print(bounces,(3/5*height))
    bounces += 1
    height = height * (3/5)
