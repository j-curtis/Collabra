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
							#all keywords are internalized as lowercase and are stored only once in the list  

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
		#adds a keyword but only if it isn't already in the keywords list
		#makes lowercase before adding it so that all keywords are lowercase internally
		if not keyword.lower() in self.keywords:
			self.keywords.append(keyword.lower())

	def addKeywords(self,list_of_keywords):
		#adds each keyword in list_of_keywords
		for keyword in list_of_keywords:
			self.addKeyword(keyword)

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
		
	def getObjects(self,list_of_objNames=[]):
		#retuns a list of objects in the database with an objName in the list 
		#order of the objects is the same as the order of the objNames in the passed list
		return [self.entries[k] for k in list_of_objNames if k in self.entries.keys()]

#these functions perform a search or sort on a dictionary of objects 
#they are not part of the dictionary object but the intention is that they be used to search through the database dictionary
#the first argument is obj_dict and is the dictionary of objects fed in
#the second argument is keys_list and is an ordered list of dictionary keys 
#subsequent arguments are various query related arguments 
#returns a list of keys that represents the keys satisfying the query in the specified order 

#searches in the list of keys for objects that are in the set of specified objTypes
#returns order is arbitrary
def searchObjTypes(keys_list,obj_dict,list_of_objTypes=[".obj.pub",".obj.pub.article",".obj.pub.book"]):
	"""looks through keys_list and picks the entries out of obj_dict that have an objType in the passed list
	return order is arbitrary"""
	return [k for k in keys_list if k in obj_dict.keys() and obj_dict[k].objType in list_of_objTypes]

#searches through the list of keys for objects that have keywords within the query set
#only can search through objects that have a keyword field defined 
#return order is sorted by number of matching keywords (most to least)
def searchKeywords(keys_list,obj_dict,list_of_keywords=[]):
	"""searches through keys_list and picks the entries out of obj_dict that have keywords in the list_of_keywords set
	return order is sorted from most matching keywords to fewest
	search is case insensitive"""
	#we make the query set case insensitive by converting all the strings to lowercase
	list_of_keywords_lower = map(lambda x: x.lower(), list_of_keywords)

	#we define a function that checks how many elements are in common between the query set and the keywords set 
	def numInCommon(list1,list2):
		return len(set(list1)&set(list2))
	
	#get keys whose value has some intersection with the query set 
	r_keys = filter(lambda x: numInCommon(obj_dict[x].keywords,list_of_keywords) > 0, keys_list)
	r_keys.sort(key=lambda x: numInCommon(obj_dict[x].keywords,list_of_keywords) ,reverse=True)

	return r_keys

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
_debug_obj = Object("_debug_obj")

_debug_pub = Publication(objName="_debug_pub",title="A Publication",author="First Author",year=2016)
_debug_pub.addKeywords(["test","debug"])

_debug_article = Article(objName="_debug_article",title="An Article",author="First Author",year=2017,journal="A Journal",volume="300",number="40")
_debug_article.addKeywords(["test","debug","article"])

_debug_book = Book(objName="_debug_book",title="A Book",author="First Author",year=2018,publisher="A Publisher")
_debug_book.addKeywords(["test","debug","book"])

_debug_db = Database(objName="_debug_db")
_debug_db.addObject(_debug_obj)
_debug_db.addObject(_debug_pub)
_debug_db.addObject(_debug_article)
_debug_db.addObject(_debug_book)

def main():
	print _debug_db
	pubs=searchObjTypes(_debug_db.entries.keys(),_debug_db.entries)
	print pubs
	articles = searchKeywords(pubs,_debug_db.entries,list_of_keywords=["article"])
	print articles


if __name__ == "__main__":
	main()











