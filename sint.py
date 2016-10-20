from uint import UInt

class SInt(UInt):
	"""Manipulation des entiers non signes"""
	
	def __init__(self, arg):
		UInt.__init__(self,arg)
		print("t) Creation d'un SINT a " + str(self.nbBytes) + " octets : " + self.binaire)
		self.signe=self.binaire[0]

	def __getsigne__():
		return self.signe

	def __rshift__():
		pass

	def extend():
		pass

	def compare(self, cmp):
		bfa=self.binaire[0]
		bfb=cmp.binaire[0]

		if bfa == bfb: #leur bit de poid fort est le meme, donc meme signe
			return super.compare(cmp)
		else:
			if bfa>bfb: #si bfa est negatif
				return "01"
			else:
				return "10"

	def complement(self):
		comp=self.binaire
		print "init - " + comp

		comp=UInt.complement(self)
		print "complement - " + comp

		#creation du nombre 1 en fonction de la taille voulue
		a=SInt(self.nbBytes)
		a.binaire=""
		for x in xrange(0,a.__len__()-1):
			a.binaire+="0"
		a.binaire+="1"


		comp=self.__add__(a)
		print "+1 - " + comp

		return comp

