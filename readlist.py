# read line by line
f = open("keycodes.txt","r")

# read first line
keycodelist = []
'''
newcode = f.readline()
while newcode != "":
    newcode = f.readline()
    keycodelist.append(newcode)
'''
for newcode in f:
    keycodelist.append(newcode[:-1])

# check user code is correct
usercode = input("Enter the keycode ")

if usercode in keycodelist:
    print("Success")
else: 
    print("Incorret") 

    
