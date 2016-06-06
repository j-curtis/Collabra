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
_debug_pub = Publication(objName="debug_pub",title="A Publication",author="First Author",year=2016)
_debug_article = Article(objName="debug_article",title="An Article",author="First Author",year=2017,journal="A Journal",volume="300",number="40")
_debug_book = Book(objName="debug_book",title="A Book",author="First Author",year=2018,publisher="A Publisher")

def main():
	print _debug_obj
	print _debug_obj.toJSONString()
	print
	print _debug_pub
	print _debug_pub.toJSONString()
	print
	print _debug_article
	print _debug_article.toJSONString()
	print
	print _debug_book
	print _debug_book.toJSONString()

if __name__ == "__main__":
	main()











