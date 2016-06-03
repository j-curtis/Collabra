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
		self.entriesSorted = []	#this is a list of the keys in the dictionary, sorted by the most previous sorting method

	#A method for printing to output 
	def __str__(self):
		return "Database: "+str(self.name)+", entries: "+str(self.entryCount)

	#this method adds an entry
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
		self.entryCount = len(self.entries.keys())	#update size 
		self.entriesSorted.append(publication.refKey)	#updates list of keys. Appends added key to the end of the sorted list 
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
		self.entriesSorted = list(self.entries.keys())	#updates the list of keys. Goes to default sorting (could be random) 
		if verbose:
			print "Removed publicaiton \'"+refKey+"\'"
		return True

	#this method returns the publication with the requested refKey
	def getRefKey(self,refKey,verbose=False):
		#if the requested key is not in the database, None is returned 
		if refKey in list(self.entries.keys()):
			return self.entries[refKey]
		else:
			if verbose:
				print "Error: refKey \'"+refKey+"\' not found in database"			
			return None

	
	#These methods sort the database dictionary keys 
	#This method accepts a set of keywords (keywords_set)
	#it orders the list of sorted keys from most to fewest keywords in common unless invert is true (default is false)
	#in which case it orders from fewest in common to most in common
	def sortByKeywordMatches(self,keywords_query_set,invert=False):
		self.entriesSorted = sorted(self.entriesSorted,\
	     key= lambda x: self.entries[x].keywords.intersection(keywords_query_set), reverse=invert)


debug_database = Database("debug_database")
debug_database.addPublication(PublicationClasses.debug_article)
debug_database.addPublication(PublicationClasses.debug_book)

def main():
	print debug_database
	print debug_database.entriesSorted
	debug_database.sortByKeywordMatches({"article"})
	print debug_database.entriesSorted
	debug_database.sortByKeywordMatches({"article"},invert = True)
	print debug_database.entriesSorted

if __name__ == "__main__":
	main()



