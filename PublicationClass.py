#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for publications 
#There will be a single publication class 
#there are also methods to convert to a json string and back so that each object can be converted to a standard format for storage
import json

class Publication:
	"""
	Class for publication objects. 
	Initializiation requires a user input string for it's reference key.
	"""
	def __init__(self, refKey):
		#all attributes are strings/ints/lists of strings/ints 
		#refKey must be unique
		self.refKey = refKey #unique identifier for internal/citation reference
		self.pubType = None	#the type of publication. This is a constant for each class 
		self.keywords = []	#optional list of keywords relevant for searching for the article
		self.authors = []	#string(list)/authors 
		self.title = None	#string/title 
		self.journal = None	#string/journal name 
		self.volume = None	#string/journal volume
		self.number = None #string/journal number
		self.year = None #int/year of publication
		self.publisher = None #string/publisher name
		self.location = None #string/publishing location
		self.doi = None #string/d.o.i. code 
		self.link = None #string/weblink
		self.notes = [] #string(list)/note,comment

	def __str__(self):
		#method for quick printing object details 
		return "Publication: " + str(self.refKey) + ", type: " + str(self.pubType)+"\n\t Keywords: " + str(self.keywords)

	def toJSONString(self):
		#We create a string representing the JSON format of this object 
		obj_dict = self.__dict__	#convert class to dictionary object 
		return json.dumps(obj_dict)	#converts object to dictionary then to a string 

	@classmethod
	def fromJSONString(cls,JSONString):
		#this method will serve as a constructor for a Publication object by parsing a JSON string 
		#it will be overloaded upon inheritance
		obj_dict = json.loads(JSONString)
		obj_class = cls(refKey = obj_dict["refKey"])
		
		#we take advantage of the fact that each object in python has a dictionary representation to fill all the other attributes as well
		for key in obj_dict.keys():
			obj_class.__dict__[key] = obj_dict[key]

		return obj_class

	#PREDEFINED PUBLICATION TYPES WITH REQUIRED FIELDS
	
	#ARTICLE TYPE
	#Required fields are 
	#Author, Title, Journal, Journal volume, Journal number, Publication year
	#Further attributes include 
	#DOI, Link, Keywords, and Notes
	#One author is required but other authors can be added 
	def addArticle(self,author,title,journal,volume,number,year):
		self.pubType = "article"
		self.authors.append(author)
		self.title = title
		self.journal = journal
		self.volume = volume
		self.number = number
		self.year = year

	#BOOK TYPE
	#Required attributes are 
	#Author, Title, Publisher, Publishing Year
	#Additional attributes are 
	#Link, Keywords, and Notes
	#One author is required but more can be added 
	def addBook(self,author,title,publisher,year):
		self.pubType = "book"
		self.authors.append(author)
		self.title = title
		self.publisher = publisher
		self.year = year

	#Methods for adding optional fields

	def addAuthor(self,author):
		self.authors.append(author)

	def addDOI(self,doi):
		self.doi = doi

	def addLink(self,link):
		self.link = link

	def addNote(self,note):
		self.notes.append(note)

	def addLocation(self,location):
		self.location = location

	def addKeyword(self,keyword):
		#this adds a keyword to a set 
		#all keywords are internalized as completely lowercase
		#this means keywords are NOT SENSITIVE TO CASE
		self.keywords.append(keyword.lower())

debug_pub_article = Publication("debug_pub_article")
debug_pub_article.addArticle(author="First Author",title="An Article",journal="Prestigous Journal",volume="300",number="43",year=2016)
debug_pub_article.addKeyword("article")
debug_pub_article.addKeyword("test")
debug_pub_article.addKeyword("debug")

debug_pub_book = Publication("debug_pub_book")
debug_pub_book.addBook(author="First Author",title="A Book",publisher="Good Publisher",year=2017)
debug_pub_book.addKeyword("book")
debug_pub_book.addKeyword("test")
debug_pub_book.addKeyword("debug")

def main():
	print debug_pub_article
	print debug_pub_article.toJSONString()
	print
	print debug_pub_book
	print debug_pub_book.toJSONString()

if __name__ == "__main__":
	main()