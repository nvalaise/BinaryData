import sys
from random import randint
from math import pow

class Mot:
	"""Type de base des mots binaire"""

	def __init__(self, arg):
		if arg <= 0:
			print("Error : Cannot init binaire with nbBytes <= 0");
			sys.exit();
		self.nbBytes = arg
		self.binaire=""
		for x in xrange(0,self.nbBytes*8):
			self.binaire+=str(randint(0,1))
			pass
		print("Creation d'un mot a " + str(self.nbBytes) + " octets : " + self.binaire)

	def __setnbBytes__(self,arg):
		print("Read only")

	def __getnbBytes__(self):
		return self.nbBytes

	def __setbinaire__(self,arg):
		self.binaire=arg
		return self.__getbinaire()

	def __getbinaire__():
		return self.binaire

	def valeur(self):
		cpt=0
		hexa="0x"
		tmp=""
		for x in xrange(0,self.__len__()):
			cpt+=1
			tmp+=self.binaire[x]
			if cpt==4:
				hexa+=self.binToHexa(tmp)
				cpt=0
				tmp=""
		return hexa

	def binToHexa(self, bloc):
		sumHexa=0
		for x in xrange(0,4):
			binPow = int(bloc[x]) * pow(2,3-x)
			sumHexa+=binPow
			#print("b " + str(bloc[x]) + " pow = " + str(binPow))
		print("bloc = " + bloc + " hexa = " + str(sumHexa))

		#On compte de 0 a 9 puis de A a F
		if sumHexa<10:
			return str(int(sumHexa));
		elif sumHexa==10:
			return "A"
		elif sumHexa==11:
			return "B"
		elif sumHexa==12:
			return "C"
		elif sumHexa==13:
			return "D"
		elif sumHexa==14:
			return "E"
		elif sumHexa==15:
			return "F"

	def __len__(self):
		return (self.nbBytes*8)

	def compare(self, cmp):
		sizeSelf=self.__len__()
		sizeCmp=cmp.__len__()

		if sizeSelf!=sizeCmp :
			print("Error : sizes are differents");
			sys.exit();
		for x in range(0,sizeSelf):
			#print(str(x) + " => {" + str(self.binaire[x]) + " , " + str(cmp.binaire[x]) + "}")
			if self.binaire[x]>cmp.binaire[x]:
				return "10"
			elif self.binaire[x]<cmp.binaire[x]:
				return "01"
		return "00"

	def __eq__(self, cmp):
		return (self.compare(cmp) == "00")

	def __rshift__(self):
		tmp="0"
		for x in range(0,self.__len__()-1):
			tmp+=self.binaire[x]
		self.binaire=tmp

	def __lshift__(self):
		tmp=""
		for x in range(0,self.__len__()-1):
			tmp+=self.binaire[x+1]
		tmp+="0"
		self.binaire=tmp

	def complement(self):
		tmp=""
		for x in range(0,self.__len__()):
			if self.binaire[x]=="1" :
				tmp+="0"
			else :
				tmp+="1"
		self.binaire=tmp

	def extend(self, k):
		bytes=max(1, max(k, self.nbBytes))
		# completer avec des 0 a gauche

	def reduce(self, k):
		bytes=max(1, min(k, self.nbBytes))
		# prendre la partie de gauche

	def cast(self, k):
		if k >= p:
			self.extend(k)
		else :
			self.reduce(k)
	
	def relativExtension(self, k):
		if k >= 0 :
			self.extend(k+self.nbBytes)
		else :
			self.reduce(k+self.nbBytes)
