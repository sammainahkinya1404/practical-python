bills_thickness=0.11*0.001
sears_height=442
num_bills=1
day=1

while num_bills*bills_thickness<sears_height:
    print(day,num_bills*bills_thickness)
    day=day+1
    num_bills=num_bills*2
    
print("number of days",day)
print("number of bills",num_bills)
print("Final Height",num_bills*bills_thickness)
    
    