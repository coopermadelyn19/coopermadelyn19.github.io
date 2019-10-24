

def getrate(speed):
    '''Calculate the cost of a speeding ticket in Georgia'''
    # process
    if speed<75:
        message = "No ticket"
    elif speed<80:
        message = "Your ticket is $25"
    elif speed<84:
        message = "Your ticket is $100"
    elif speed<89:
        message = "Your ticket is $125"
    elif speed<94:
        message = "Your ticket is $150"
    elif speed<104:
        message = "Your ticket is $500"
    else: 
        message = "You get arrested"
    return message
#test
print(getrate(103))

    