class Data:
	
	def __init__(self,name,run,amount):
		self.name=name
		self.run=run
		self.amount=amount

	def deposit(self):
		print("Su saldo: ",self.amount)
		amount=int(input("Ingrese monto que quiere depositar: \n"))
		if amount>0:
			self.amount+=amount
		else:
			print("Indique un valor coherente")

	def display(self):
	    print("\nNombre: ",self.name)
	    print("Run: ",self.run)
	    print("Dinero disponible: ",self.amount)
