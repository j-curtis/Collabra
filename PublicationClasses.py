#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for publications 
#There will be a base publication class 
#We will derive various types of publications from it
#but all attributes will be determined from the base class and set to None
#each class will use some of the attributes 
class Publication:
	"""
	Base class for publication objects. 
	Initializiation requires a user input string for it's reference key.
	"""
	pubType = None

	def __init__(self, refKey):
		self.refKey = refKey #unique identifier for internal/citation reference
		self.keywords = set([])	#optional set of keywords
		#all publications can have keywords
		#keywords is a set of strings that are relevant to the entry 
		self.authors = None	#string(list)/authors 
		self.title = None	#string/title 
		self.journal = None	#string/journal name 
		self.volume = None	#int/journal volume
		self.number = None #int/journal number
		self.year = None #int/year of publication
		self.month = None #int/month of publication
		self.publisher = None #string/publisher name
		self.location = None #string/publishing location
		self.doi = None #string/d.o.i. code 
		self.link = None #string/weblink
		self.note = None #string/note,comment



	def __str__(self):
		#method for printing object 
		return "Publication: " + str(self.refKey) + ", type: " + str(self.pubType)+"\n\t Keywords: " + str(self.keywords)

	def addKeyword(self,keyword):
		#this adds a keyword to a set 
		#all keywords are internalized as completely lowercase
		#this means keywords are NOT SENSITIVE TO CASE
		self.keywords.add(keyword.lower())

#Article class inherits from publication 
class Article(Publication):
	"""
	Article class. Inherits from Publication class.
	"""
	pubType = "article"

	#Required attributes are
	#Author, Title, Journal, Journal volume, Journal number, Publication year
	#Further attributes include 
	#DOI, Link, Keywords, and Notes
	#One author is required but other authors can be added 
	#in the overloaded constructor we set certain values as required
	def __init__(self,refKey,author,title,journal,volume,number,year):
		#first we call the base class init
		Publication.__init__(self,refKey)
		##now we initialize the specific attributes
		self.authors = []
		self.authors.append(author)
		self.title = title
		self.journal = journal
		self.volume = volume
		self.number = number
		self.year = year

	def addAuthor(self,author):
		self.authors.append(author)
		self.authorsCount = len(self.authors)

	def addDOI(self,doi):
		self.doi = doi

	def addLink(self,link):
		self.link = link

	def addNote(self,note):
		self.note = note


#Book class inherits from publication
class Book(Publication):
	"""
	Book class. Inherits from Publication class.
	"""
	pubType = "book"

	#required attributes are 
	#Author, Title, Publisher, Publishing Year
	#Additional attributes are 
	#Link, Keywords, and Notes
	#One author is required but more can be added 
	#in the overloaded constructor we set all possible fields to empty or None
	def __init__(self,refKey,author,title,publisher,year):
		#first we call the base class init
		Publication.__init__(self,refKey)
		##now we initialize the specific attributes
		self.authors = []
		self.authors.append(author)
		self.title = title
		self.publisher = publisher
		self.year = year

	
	def addAuthor(self,author):
		self.authors.append(author)

	def addLocation(self,location):
		self.location = location

	def addDOI(self,doi):
		self.doi = doi

	def addLink(self,link):
		self.link = link

	def addNote(self,note):
		self.note = note


#Some default debugging instances of the provided classes 
debug_publication = Publication("debug_publication")
debug_publication.addKeyword("Debug")
debug_publication.addKeyword("Publication")
debug_publication.addKeyword("Test")

debug_article = Article(refKey="debug_article",title="An Article",author="First Author",journal="PRL",volume=140,number=30,year=2016)
debug_article.addDOI("DOI")
debug_article.addLink("www.thelink.com")
debug_article.addAuthor("Second Author")
debug_article.addKeyword("debug")
debug_article.addKeyword("article")
debug_article.addKeyword("test")

debug_book = Book(refKey="debug_book",author="First Author",title="A Book",publisher="The Publisher",year=2017)
debug_book.addLink("www.thelink.com")
debug_book.addAuthor("Second Author")
debug_book.addKeyword("debug")
debug_book.addKeyword("book")
debug_book.addKeyword("test")

def main():
	print debug_publication
	print
	print debug_article
	print 
	print debug_book
	print 

if __name__ == "__main__":
	main()