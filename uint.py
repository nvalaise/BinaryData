from mot import Mot

class UInt(Mot):
	"""Manipulation des entiers non signes"""
	
	def __init__(self, arg):
		Mot.__init__(self,arg)
		print("o) Creation d'un UINT a " + str(self.nbBytes) + " octets : " + self.binaire)


	def __add__(self, op):
		retenu=False
		res=""

		print "p) " + self.binaire

		for x in range(self.nbBytes*8-1,-1, -1):
			sum=0
			if retenu:
				sum+=1
				retenu=False
			#print "q) x = " + str(x) + " ; UINT(x) = " + self.binaire[x]
			#print "q) x = " + str(x) + " ; UINT(x) = " + op.binaire[x]

			sum+=int(self.binaire[x]) + int(op.binaire[x])
			#print "sum = " + str(sum)
			if sum==1 or sum==0:
				res=str(sum)+res
			elif sum==2:
				res="0"+res
				retenu=True
			elif sum==3:
				res="1"+res
				retenu=True
			else:
				print "Error"
				return

		return res



	def __mul__():
		pass

	def __lt__(self, cmp):
		return self.compare(cmp)
