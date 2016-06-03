#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for the database of publications
#It will contain a set of publications, their refKeys, and their keywords 
#We will implement a simple dictionary structure for managing the files, as we don't expect it to be VERY large (~500 max)
import PublicationClasses

class Database:
	"""
	Database class. Contains a dictionary of all Publication objects with keys provided by refKeys.
	Will handle addition, removal, and retrieval of Publication objects.
	"""

	def __init__(self,name):
		#Each database will be given a name 
		self.name = name
		self.entryCount = 0	#number of entries in the database
		#We initialize an empty dictionary
		self.entries = {}

	#A method for printing to output 
	def __str__(self):
		return "Database: "+str(self.name)+", entries: "+str(self.entryCount)

	#This method adds an entry
	def addPublication(self,publication,verbose=False):
		#publication is an instance of a Publication object or derived Publication object 
		#verbose is an option that, when true will print a bit more information about failed/successful attempts to add entries
		#first it checks to see if required entries are filled 
		if not publication.requiredFieldsCheck():
			if verbose: 
				print "Error: publication with refKey \'"+publication.refKey+"\' does not have required fields filled"
			return False

		#then it checks to make sure the key is not already in use 
		#returns true if addition was succesful, else returns false
		if publication.refKey in list(self.entries.keys()):
			if verbose:
				print "Error: refKey \'"+publication.refKey+"\' is already in use"
			return False

		self.entries[publication.refKey] = publication
		self.entryCount = len(list(self.entries.keys()))	#update size 
		if verbose:
			print "Added publication \'"+publication.refKey+"\'"
		return True

	#this method removes an entry with the specified refKey
	def removePublication(self,refKey,verbose=False):
		#we first check it actually is in the database
		if refKey not in list(self.entries.keys()):
			if verbose:
				print "Error: refKey \'"+refKey+"\' not found in database"
			return False

		#it is in the database so we remove it 
		del(self.entries[refKey])
		self.entryCount = len(list(self.entries.keys()))
		if verbose:
			print "Removed publicaiton \'"+refKey+"\'"
		return True



debug_database = Database("debug_database")
debug_database.addPublication(PublicationClasses.debug_article)
debug_database.addPublication(PublicationClasses.debug_book)

def main():
	print debug_database
	debug_database.removePublication("debug_article",verbose=True)
	debug_database.removePublication("fake_article",verbose=True)
	print debug_database

if __name__ == "__main__":
	main()



