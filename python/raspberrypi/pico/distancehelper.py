class distancetools(object):

    def __init__(self):
        self.totalcentimeters = 0
        self.cmtoinch = const(0.39370079)
        self.meters = "0"
        self.centimeters = "0"
        self.feet = "0"
        self.inches = "0"
    
    def set(centimeters):
        self.totalcentimeters = totalcentimeters
        s = "{0}".format(totalcentimeters / 100)
        self.meters = "{0}".format(s[:s.find(".")])
        self.centimeters = "{0}".format(totalCentimeters - (int(self.meters) * 100))
        totalinches = int(self.centimeters) * self.cmtoinch
        s = "{0}".format(totalinches / 12)
        self.feet = "{0}".format(s[:s.find(".")])
        self.inches = "{0}".format(totalInches - (int(self.feet) * 12))