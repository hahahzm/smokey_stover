def isDate(mm, dd, yy):
    if (mm > 12):
        return False
    if ((mm == 1) or (mm == 3) or (mm == 5) or (mm == 7) or (mm == 8) or (mm == 10) or (mm == 12)):
        if (dd > 31):
            return False
    elif (mm == 2):
        if (dd > 28):
            return False
    else:
        if (dd > 30):
            return False
            
    return True

def answer(x, y, z):
    # your code here
    count = 0
    result = ""
    if (isDate(x,y,z)) :
        mm = x
        dd = y
        yy = z
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (isDate(x,z,y)) :
        mm = x
        dd = z
        yy = y
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (isDate(z,y,x)):        
        mm = z
        dd = y
        yy = x
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (isDate(y,x,z)) :
        mm = y
        dd = x
        yy = z
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (isDate(z,x,y)) :
        mm = z
        dd = x
        yy = y
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (isDate(y,z,x)) :
        mm = y
        dd = z
        yy = x
        if (result == ""):
            result = "%02d/%02d/%02d" % (mm, dd, yy)
        elif (result != "%02d/%02d/%02d" % (mm, dd, yy)):
            return "Ambiguous"
    if (count > 1):
        return result
        
    


while (True):
    xx = int(input("xx: "))
    yy = int(input("yy: "))
    zz = int(input("zz: "))

    print answer(xx,yy,zz) + "\n"
