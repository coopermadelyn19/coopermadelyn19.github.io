
# test on while loop
'''
go = input("Do you want to continue? Yes or no? ")


while go == "yes":
    print("I am in the while loop")
    go = input("Do you still want to continue? Yes or no? ")

while True:
    print("I am in the while loop")
    go = input("If you don't want to continue, enter no")
    if go == "no":
        break # break out of the loop

print("Okay I am out of the loop")
'''

count = 1 
while count>0:
    print(count)
    count -=1