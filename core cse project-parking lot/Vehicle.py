'''creating a vehicle object and it has properties colour and registation number'''
class Vehicle:  
	
	def __init__(self,regno,color):

		self.color =  color                 

		self.regno = regno


'''creating a car object and inhering the properties of vehicle'''

class Car(Vehicle):

	def __init__(self, regno, color):

		Vehicle.__init__(self, regno, color)

	