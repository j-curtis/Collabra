#Collabra 
#Jonathan Curtis, Jun 5 2016 

#this file details the basic objects in the program
#we start with a base class object (Object)
#Object can then be derived into the various classes such as Publication, Database, and other possible classes 
#all objects will have a name attribute (unique) and a type identifier (quick string identifying the class)
#all objects will have a string representation defined and a to/from JSON method defined 

#object types will be of the form 'obj.derivedTypeName'
#names must be unique for each object in the current scope 
#the string representation will be given as 'objType/objName'

import json 

#Base class of the program 
class Object:
	def __init__(self,objName):
		#object types will be of the form '.obj.derivedTypeName'
		#names must be unique for each object in the current scope
		self.objName = objName 
		self.objType = ".obj"

	def __str__(self):
		#the string representation will be given as 'objType/objName'
		return self.objType+"/"+self.objName

	def toJSONString(self):
		#converts the object to a JSON formatted string representation
		return json.dumps(self.__dict__)

	@classmethod
	def fromJSONString(cls,JSONString):
		#constructs an object given its JSON formatted string representation 
		#we take advantage of the fact that python can represent a class as a dictionary internally 
		obj_dict = json.loads(JSONString)
		obj_class = cls(objName = obj_dict["objName"])

		for attr in list(obj_dict.keys()):
			obj_class.__dict__[attr] = obj_dict[attr]

		return obj_class

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
#constructor has all required fields as required arguments 
class Article(Publication):
	def __init__(self,objName,title,author,year,journal,volume,number):
		Publication.__init__(self,objName,title,author,year)

		self.objType = self.objType + ".article"
		
		self.journal = journal
		self.volume = volume 
		self.number = number 

#a derived class for book publications 
#constructor has all required fields as required arguments 
class Book(Publication):
	def __init__(self,objName,title,author,year,publisher):
		Publication.__init__(self,objName,title,author,year,publisher)

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













