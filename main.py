from mot import Mot
from uint import UInt
from sint import SInt

a = Mot(1)
b = Mot(1)

print "f) " + a.valeur()

print "g) " + a.binaire
a.__rshift__()
print "h) " + a.binaire
a.__lshift__()
print "i) " + a.binaire
a.complement()
print "j) " + a.binaire

print "k) __eq__ : " + str(a.__eq__(b))
b.binaire=a.binaire
print "l) __eq__ : " + str(a.__eq__(b))


a.__setnbBytes__(3)
print "m) " + str(a.nbBytes)
#print a.compare(b)
#print b.compare(a)
#print a.compare(a)

c = UInt(1)
print "n) " + c.binaire

d = UInt(1)

print "r) " + c.binaire + " + " + d.binaire + " = " + c.__add__(d)

print "s) " + c.binaire + " > " + d.binaire + " ? " + c.compare(d)

e = SInt(1)
print "u) " + e.complement()

f = SInt(1)
print "s) " + e.binaire + " > " + f.binaire + " ? " + e.compare(f)
