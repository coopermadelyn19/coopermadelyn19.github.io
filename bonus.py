numgallons=input("How many gallons of gas can the car hold? ")
nummiles=input("How many miles can the car be driven on a full tank? ")
gasprice=float(2.720)

gasmileage= float(numgallons) * float(nummiles) * float(gasprice)

print("The cost of gas per mile is "+str(gasmileage))


