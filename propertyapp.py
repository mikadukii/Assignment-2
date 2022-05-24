# e2100306
# propertyapp

# class property
class property:
    # initialize properties variable
    def __init__(self, location, price, propertytype, size):
        self.location = location
        self.price = price
        self.propertytype = propertytype #apartment, bungalow, condomonium
        self.size = size
    
    # getter for the variables
    # getter for location
    def getlocation(self):
        return self.location

    # getter for price
    def getprice(self):
        return self.price
    
    # getter for propertytype
    def getpropertytype(self):
        return self.propertytype

    # getter for size
    def getsize(self):
        return self.size
    
    # setter for the variables above so it can be set
    # setter for location
    def setlocation(self, newlocation):
        self.location = newlocation

    # setter for price
    def setprice(self, newprice):
        self.price = newprice

    # setter for propertytype
    def setpropertytype(self, newpropertytype):
        self.propertytype = newpropertytype

    # setter for size
    def setsize(self, newsize):
        self.size = newsize

    # typestring to indetify property type either apartment/bungalow/condomonium
    def typestring(self):
        if self.propertytype == "A" or self.propertytype == "a":
            return "apartment"
        if self.propertytype == "B" or self.propertytype == "b":
            return "bungalow"
        if self.propertytype == "C" or self.propertytype == "c":
            return "condomonium"

    # to calculate annual tax based on property type
    def annualtax(self):
        taxannual = 0
        if (self.propertytype.lower() == "a"):
            taxannual = self.price * 2.5/100;
            
        elif (self.propertytype.lower() == "b"):
            taxannual = self.price * 4.5/100;
            
        elif (self.propertytype.lower() == "c"):
            taxannual = self.price * 3.5/100;

        return taxannual
    
    # returns true if both properties are equal
    def _eq_(self, PropertyObject):
        if self.PropertyObject.size == PropertyObject.size and self.PropertyObject.location == PropertyObject.location and self.PropertyObject.type == PropertyObject.type:
            return True
        else:
            return False

    # returns true if this property have size less than the parametric property's size
    def _lt_(self, PropertyObject):
        if self.PropertyObject.size < PropertyObject.size:
            return True
        else:
            return False

    # returns true if this property have size less than or equal to the paramateric property's size
    def _le_(self, PropertyObject):
        if self.PropertyObject.size <= PropertyObject.size:
            return True
        else:
            return False

    # string method for details of property
    def __str__(self):
        return self.typestring().capitalize() + "," + str(self.size) + " square feet, at " \
        + self.location.capitalize() + ", costing $" + "{:.2f}".format(self.price)

class PropertyList:
    # initial consist of groupname and property collection
    def __init__(self, groupname):
        self.groupname = groupname
        self.propertyCollection = []

    # getter for group name and property collection
    def getgroupname(self):
        return self.groupname

    # getter for property collection
    def getpropertycollection(self):
        return self.propertyCollection

    # setter for group name for able set group name
    def settername(self, newgroupname):
        self.groupname = newgroupname

    # to be able to add to property collection by using append
    def addProperty(self, PropertyObject):
        self.propertyCollection.append(PropertyObject)
    
    # use len to check to count number of properties
    def noOfProperties(self):
        numofprop = len(self.propertyCollection)

        return numofprop

    # to check all properties
    def allProperties(self):
        view = ""
        for i in range(len(self.propertyCollection)):
            view = view + str(self.propertyCollection [i]) + "\n"
        
        return view

    # to calculate total price
    def totalPrice(self):
        total = 0
        for i in range(len(self.propertyCollection)):
            total = total + self.propertyCollection[i].getprice()

        return total
        
    # to show most expensive property
    def mostExpensiveProperty(self):
        priceCollection = [] 
        for i in range(len(self.propertyCollection)):
            # to get price from pricecollection
            priceCollection.append(self.propertyCollection[i].getprice())
        # to get max number from price collection
        maximum = max(priceCollection) 
        # to be able find maximum from the index
        index = priceCollection.index(maximum)
        # to be able view and show max price
        view = str(self.propertyCollection[index])

        return view

    # to find property by type
    def findPropertyByType(self, type):
        result = ""
        for i in range(self.noOfProperties()):
            if self.propertyCollection[i].getpropertytype() == type:
                result = result + str(self.propertyCollection[i]) + "\n" 
        
        return result

    # to sell property once sold it removes from index
    def sellProperty(self, index):
        if index >= self.noOfProperties():
            return "none"
        else:
            del self.propertyCollection[index]

    # to sort properties from price, tax, size
    # sort case method: insertion sort  
    def sortedProperty(self, sortparameter):
        typecollection = []
        # sort by price
        if sortparameter == "price":
            for i in range(len(self.propertyCollection)):
                typecollection.append(self.propertyCollection[i])

            for i in range(len(typecollection)):
                key = typecollection[i]
                j = i-1
                while j >=0 and key.getprice() < typecollection[j].getprice():
                    typecollection[j+1] = typecollection[j]
                    j -= 1
                typecollection [j+1] = key
        
        # sort by tax        
        elif sortparameter == "tax":
            for i in range(len(self.propertyCollection)):
                typecollection.append(self.propertyCollection[i])

            for i in range(len(typecollection)):
                key = typecollection[i]
                j = i-1
                while j >=0 and key.annualtax() < typecollection[j].annualtax():
                    typecollection[j+1] = typecollection[j]
                    j -= 1
                typecollection [j+1] = key

        # sort by size       
        elif sortparameter == "size":
            for i in range(len(self.propertyCollection)):
                typecollection.append(self.propertyCollection[i])

            for i in range(len(typecollection)):
                key = typecollection[i]
                j = i-1
                while j >=0 and key.getsize() < typecollection[j].getsize():
                    typecollection[j+1] = typecollection[j]
                    j -= 1
                typecollection [j+1] = key

        return typecollection

    # save file
    def savetofile(self, filename):
        datastr = ""
        for data in self.propertyCollection :
            location = data.getlocation()
            price = data.getprice()
            propertytype = data.getpropertytype()
            size = data.getsize()
            datastr = datastr + location + "," + str(price) + "," + propertytype + "," + str(size)

        fileopen = open(filename, 'w')
        fileopen.write(datastr)
        fileopen.close()


    # load from the file
    def loadfromfile(self, filename):
        self.propertyCollection = []
        fileopen = open(filename, 'r')
        for data in fileopen:
            dataproperty = data.split(",")
            location = dataproperty[0]
            price = float(dataproperty[1])
            propertytype = dataproperty[2]
            size = int(dataproperty[3])
            propertyobject = property(location, price, propertytype, size)
            self.addProperty(propertyobject)

        fileopen.close()