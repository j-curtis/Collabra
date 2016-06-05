#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for the database of publications
#It will contain a set of publications, their refKeys, and their keywords 
#We will implement a simple dictionary structure for managing the files, as we don't expect it to be VERY large (~500 max)
#It doesn't do searching/sorting just stores the entries 
#It also handles the file I/O of storing/loading the database files 
import PublicationClass
import json

class Database:
	"""
	Database class. Contains a dictionary of all Publication objects with keys provided by refKeys.
	Will handle addition, removal, and retrieval of Publication objects.
	"""

	def __init__(self,name):
		#Each database will be given a name 
		self.name = name
		self.entries = {}	#dictionary of all publications, with keys as the keyRefs
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
	
	#this method turns the entire database into a string JSON representation
	def toJSONString(self):
		#first we convert all the Publication entries into their JSON string representations
		#we then add them to a list of the JSON string representations 
		entries_list = []

		for key,value in self.entries.iteritems():
			entries_list.append(value.toJSONString())

		obj_dict = self.__dict__
		obj_dict["entries"] = entries_list

		return json.dumps(obj_dict)


	#this method loads from a JSON string object 
	@classmethod
	def fromJSONString(cls,JSONString):
		#Frist we convert the JSON string into a dictionary
		obj_dict = json.loads(JSONString)
		obj_class = cls(obj_dict["name"])

		#we have recreated the database, but it is empty
		#now we loop through the list and add entries 
		for entry in obj_dict["entries"]:
			publication = PublicationClass.Publication.fromJSONString(entry)
			obj_class.addPublication(publication)

		return obj_class
		
debug_database = Database("debug_database")
debug_database.addPublication(PublicationClass.debug_pub_article)
debug_database.addPublication(PublicationClass.debug_pub_book)

def main():
	print debug_database
	debug_database_JSON_string_repr =  debug_database.toJSONString()
	print debug_database_JSON_string_repr
	debug_database_from_JSON = Database.fromJSONString(debug_database_JSON_string_repr)
	print debug_database_from_JSON
	print debug_database_from_JSON.getEntry("debug_pub_article").toJSONString()
	

if __name__ == "__main__":
	main()



