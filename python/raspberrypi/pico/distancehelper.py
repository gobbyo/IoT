cmtoinch = const(0.39370079)

def getFeet(numInInches):
    i = round(numInInches)
    if i < 12:
        return 0
    else:
        s = "{0}".format(i / 12)
        i = s.find(".")
        return (int(s[:i]))
    
def getCentimeters(meters, totalCentimeters):
    return totalCentimeters - (meters * 100)

def centimetersToInches(centimeters):
    return centimeters * cmtoinch

def getInches(feet, totalInches):
    return totalInches - (feet * 12)

def getMeters(totalcentimeters):
    i = round(totalcentimeters)
    if i < 1:
        return 
    else:
        s = "{0}".format(totalcentimeters/100)
        i = s.find(".")
        return (int(s[:i]))

def main():
    totalCentimeters = 349.3245

    meters = getMeters(totalCentimeters)
    print("meters = {0}".format(meters))
    centimeters = getCentimeters(meters, totalCentimeters)
    print("centimeters = {0}".format(centimeters))

    totalInches = centimetersToInches(totalCentimeters)
    feet = getFeet(totalInches)
    print("feet = {0}".format(feet))
    inches = getInches(feet, totalInches)
    print("inches = {0}".format(inches))

if __name__ == '__main__':
    main()