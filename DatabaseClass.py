#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for the database of publications
#It will contain a set of publications, their refKeys, and their keywords 
#We will implement a simple dictionary structure for managing the files, as we don't expect it to be VERY large (~500 max)
#It doesn't do searching/sorting just stores the entries 
#It also handles the file I/O of storing/loading the database files 
import PublicationClass

class Database:
	"""
	Database class. Contains a dictionary of all Publication objects with keys provided by refKeys.
	Will handle addition, removal, and retrieval of Publication objects.
	"""

	def __init__(self,name):
		#Each database will be given a name 
		self.name = name
		self.entries = {}	#dictionary of all publications, with keys as the keyRefs
		self.sortedRefKeys = []	#sorted list of keys with most recent global sort applied
		self.entriesCount = 0	#total number of entries in the database

	#A method for printing to output 
	def __str__(self):
		return "Database: "+str(self.name)+", entries: "+str(self.entriesCount)

	#this method adds an entry
	def addPublication(self,publication,verbose=False):
		#publication is an instance of a Publication object or derived Publication object 
		#verbose is an option that, when true will print a bit more information about failed/successful attempts to add entries
		#first it checks to make sure the key is not already in use 
		#returns true if addition was succesful, else returns false
		if publication.refKey in list(self.entries.keys()):
			if verbose:
				print "Error: refKey \'"+publication.refKey+"\' is already in use"
			return False

		self.entries[publication.refKey] = publication
		self.entriesCount = len(self.entries.keys())	#update size 
		self.sortedRefKeys.append(publication.refKey)	#updates list of keys. Appends added key to the end of the sorted list 
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
		self.entryCount = len(self.entries.keys())
		self.sortedRefKeys = list(self.entries.keys())	#updates the list of keys. Goes to default sorting (could be random) 
		if verbose:
			print "Removed publicaiton \'"+refKey+"\'"
		return True

	#this method returns the publication with the requested refKey as a singleton list 
	#all have verbose which, when true (default is false) will provided more information if an error occurs
	def getEntry(self,refKey,verbose=False):
		#if the requested key is not in the database, None is returned 
		if refKey in list(self.entries.keys()):
			return self.entries[refKey] 
		else:
			if verbose:
				print "Error: refKey \'"+refKey+"\' not found in database"			
			return None
	

debug_database = Database("debug_database")
debug_database.addPublication(PublicationClasses.debug_article)
debug_database.addPublication(PublicationClasses.debug_book)

def main():
	
	

if __name__ == "__main__":
	main()



