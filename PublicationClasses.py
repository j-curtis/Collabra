#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for publications 
#There will be a base publication class 
#We will derive various types of publications from it 

class Publication:
	def __init__(self, user_key):
		"""Base class for publication objects. 
		Initializiation requires a user input string for it's reference key.
		"""
		self.ref_key = user_key 

	def __str__(self):
		#method for printing object 
		return self.ref_key





def main():
	#debugging 
	pub1 = Publication('my_first_pub_w_too_long_name')

	print pub1

if __name__ == "__main__":
	main()