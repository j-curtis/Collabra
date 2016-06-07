#Collabra 
#Jonathan Curtis, Jun 5 2016 

#this file details the basic objects in the program
#we start with a base class object (Object)
#Object can then be derived into the various classes such as Publication, Database, and other possible classes 
#all objects will have a name attribute (unique) and a type identifier (quick string identifying the class)

#object types will be of the form 'obj.derivedTypeName'
#names must be unique for each object in the current scope 
#the string representation will be given as 'objType/objName'

import jsonpickle as jsp
#we will use the module jsonpickle to encode/decode classes into JSON objects for exchange/storage 

#Base class of the program 
#uses Python 'new classes' style, which only works for Python 2.2 and up
class Object(object):
	def __init__(self,objName):
		#object types will be of the form '.obj.derivedTypeName'
		#names must be unique for each object in the current scope
		self.objName = objName 
		self.objType = ".obj"

	def __str__(self):
		#the string representation will be given as 'objType/objName'
		return self.objType+"/"+self.objName

	def toJSONString(self):
		return jsp.encode(self)

	@classmethod
	def fromJSONString(cls,JSONString):
		#constructs an object given its JSON formatted string representation 
		#uses jsonpickles decode method
		return jsp.decode(JSONString)
		
#a derived class for Publications of various types 
#we assume that all publications have an author, title, and year field
class Publication(Object):
	def __init__(self,objName,title,author,year):
		Object.__init__(self,objName)

		self.objType = self.objType + ".pub"

		self.keywords = []	#a list of words that can be used to identify the Publication 

		#required fields for all publications
		self.title = title
		self.authors = [author]
		self.year = year 

		#optional fields common to all/most publications 
		self.links = []
		self.notes = []
		self.doi = None 

	#this method adds an author to the list of authors 
	def addAuthor(self,author):
		self.authors.append(author)

	def addKeyword(self,keyword):
		self.keywords.append(keyword)

	def addNote(self,note):
		self.notes.append(note)

	def addLink(self,link):
		self.links.append(link)

	def setDOI(self,doi):
		self.doi = doi

#a derived class for article publications 
#an article, in addition to author/title/year, also requires journal name/volume/number
class Article(Publication):
	def __init__(self,objName,title,author,year,journal,volume,number):
		Publication.__init__(self,objName,title,author,year)

		self.objType = self.objType + ".article"
		
		self.journal = journal
		self.volume = volume 
		self.number = number 

#a derived class for book publications 
#a book, in addition to author/title/year, also requires a publisher
class Book(Publication):
	def __init__(self,objName,title,author,year,publisher):
		Publication.__init__(self,objName,title,author,year)

		self.objType = self.objType + ".book"

		self.publisher = publisher
		self.location = None
		self.edition = None 
		self.editor = None 

	def addLocation(self,location):
		self.location = location 

	def addEdition(self,edition):
		self.edition = edition

	def addEditor(self,editor):
		self.editor = editor 

#a derived class used to database objects
#a databse has no required attributes
#objects will be stored in a dictionary, indexed by their objName (hence objName must be unique)
class Database(Object):
	def __init__(self,objName):
		Object.__init__(self,objName)

		self.objType = self.objType+".db"

		self.entries = {}	#dictionary used to store entries, with keys provided by the objects objName attribute

	def addObject(self,obj):
		#we first check to see if the name of the object is already in the database 
		#we require all names in a database to be unique, so if the name is already present, we dont add the object 
		if obj.objName in self.entries.keys():
			return "Error: \'"+obj.objName+"\' already present in database. Cannot duplicate \'"+obj.objName+"\'"

		#it is not in the database already, we add it to the list and add the name to the names list 
		self.entries[obj.objName] = obj
		return "\'"+str(obj)+"\' added to database"

	def removeObject(self,objName):
		#removes the object in the database with name objName 
		#because the names are unique, this is relatively straightforward to do 

		#check for membership in the database 
		if not objName in self.entries.keys():
			return "Error: \'"+objName+"\' cannot be removed. \'"+objName+"\' is not a member of database"

		#it is in the database, so we remove it 
		del self.entries[objName]
		
	def getObject(self,objName):
		#returns the object in the database with the given objName 
		if objName in self.entries.keys():
			return self.entries[objName]

		#in this case, it is not in the database, so we return None 
		return None 

"""THESE CLASSES WILL BE USED TO ADD NEW FUNCTIONALITIES IN FURTHER BUILDS"""
#a derived class for Author and Author-like objects
#an author only requires a name (author name, not the object name)
class Author(Object):
	def __init__(self,objName,name):
		Object.__init__(self,objName)

		self.objType = self.objType+".author"

		self.name = name 
		self.institutions = []	#a list of institutions the author is affiliated with
		self.links = []	#a list of links relevant to the author 
		self.emails = []	#a list of emails for contacting the author 
		self.collaborators = [] #a list(is list best way?) of common collaborators (other author instances)




#sample instances of objects useful for debugging
_debug_obj = Object("debug_obj")
_debug_pub = Publication(objName="_debug_pub",title="A Publication",author="First Author",year=2016)
_debug_article = Article(objName="_debug_article",title="An Article",author="First Author",year=2017,journal="A Journal",volume="300",number="40")
_debug_book = Book(objName="_debug_book",title="A Book",author="First Author",year=2018,publisher="A Publisher")

_debug_db = Database(objName="_debug_db")
_debug_db.addObject(_debug_obj)
_debug_db.addObject(_debug_pub)
_debug_db.addObject(_debug_article)
_debug_db.addObject(_debug_book)

def main():
	print _debug_obj
	_debug_obj_JSON = _debug_obj.toJSONString()
	_debug_obj_from_JSON = Object.fromJSONString(_debug_obj_JSON)
	print _debug_obj.toJSONString()
	print _debug_obj_from_JSON.toJSONString()
	print
	print _debug_pub
	_debug_pub_JSON = _debug_pub.toJSONString()
	_debug_pub_from_JSON = Publication.fromJSONString(_debug_pub_JSON)
	print _debug_pub.toJSONString()
	print _debug_pub_from_JSON.toJSONString()
	print
	print _debug_article
	print _debug_article.toJSONString()
	print
	print _debug_book
	print _debug_book.toJSONString()
	print 
	print _debug_db
	_debug_db_JSON = _debug_db.toJSONString()
	_debug_db_from_JSON = Database.fromJSONString(_debug_db_JSON)
	print _debug_db.toJSONString()
	print _debug_db_from_JSON.toJSONString()


if __name__ == "__main__":
	main()











