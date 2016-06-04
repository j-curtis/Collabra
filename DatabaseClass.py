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

		self.allEntries = {}	#dictionary of all publications, with keys as the keyRefs
		self.allCout = 0	#total number of entries in the database
		self.allSortedKeys = []	#sorted list of keys with most recent global sort applied

		self.articleEntries = {}	#dictionary of articles with keys as the keyRefs 
		self.articleCount = 0 #number of articles in database 
		self.articleSortedKeys = [] #sorted list of article keys with most recent article sort applied

		self.bookEntries = {}	#dictionary of books with keys as the keyRefs 
		self.bookCount = 0	#number of book entries in database
		self.bookSortedKeys = [] #sorted list of articles keys with most recent book sort applied

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

	###GENERAL SORT METHODS 
	#These methods sort the database's internal entriesSorted list of keys 
	#for all, invert = True reverses sorting order (invert = False by default)
	#they do not return anything
	#they are for basic usage only, because more advanced querying can vary by pubType

	#this method alphabetically sorts by refKey
	#because refKey can be a string of any content, it will use the lexicographic string sort native to Python
	def sortByRefKey(self,invert=False):
		self.entriesSorted.sort(reverse=invert)

	#This method accepts a set of keywords (keywords_set)
	#it orders the list of keys by number of keywords intersecting with the the query set 
	#we first convert the set of query keywords to all lowercase strings
	def sortByKeywordMatches(self,query_keyword_set,invert=False):
		query_keyword_set = {x.lower() for x in query_keyword_set}
		self.entriesSorted = sorted(self.entriesSorted,\
	     key= lambda x: self.entries[x].keywords.intersection(query_keyword_set), reverse= not invert)

	#This method sorts by pubType, alphabetically 
	def sortByPubType(self,invert=False):
		self.entriesSorted = sorted(self.entriesSorted,\
			key=lambda x: self.entries[x].pubType,reverse= invert)

	###TYPE SORT METHODS
	#These methods are specialized by pubType and can yield more useful query results 
	def articleSortByRefKey(invert=False):\
		forself.entries.keys().sort(reverse=invert) )

	

debug_database = Database("debug_database")
debug_database.addPublication(PublicationClasses.debug_article)
debug_database.addPublication(PublicationClasses.debug_book)

def main():
	print debug_database
	

if __name__ == "__main__":
	main()



