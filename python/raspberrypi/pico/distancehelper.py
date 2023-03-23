cmtoinch = const(0.39370079)

def getFeet(numInInches):
    s = "{0}".format(numInInches / 12)
    return (int(s[:s.find(".")]))
    
def getCentimeters(meters, totalCentimeters):
    return totalCentimeters - (meters * 100)

def centimetersToInches(centimeters):
    return centimeters * cmtoinch

def getInches(feet, totalInches):
    return totalInches - (feet * 12)

def getMeters(totalcentimeters):
    s = "{0}".format(totalcentimeters / 100)
    return int(s[:s.find(".")])