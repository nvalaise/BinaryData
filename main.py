from mot import Mot

a = Mot(1)
b = Mot(1)

print a.valeur()

print a.binaire
a.__rshift__()
print a.binaire
a.__lshift__()
print a.binaire
a.complement()
print a.binaire

print "__eq__ : " + str(a.__eq__(b))
b.binaire=a.binaire
print "__eq__ : " + str(a.__eq__(b))


a.__setnbBytes__(3)
print a.nbBytes
#print a.compare(b)
#print b.compare(a)
#print a.compare(a)