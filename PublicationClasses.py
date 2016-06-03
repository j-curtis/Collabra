#Collabra 
#Jonathan Curtis, June 3, 2016

#This file is the class file for publications 
#There will be a base publication class 
#We will derive various types of publications from it 
class Publication:
	"""
	Base class for publication objects. 
	Initializiation requires a user input string for it's reference key.
	"""
	pubType = None

	def __init__(self, user_key):
		self.requiredFieldsFull = False	#once the required fields for a publication are filled, this is set true
		self.refKey = user_key 
		self.keywords = set([])	
		#all publications can have keywords
		#keywords is a set of strings that are relevant to the entry 


	def __str__(self):
		#we update to see if required fields are full
		self.requiredFieldsCheck()
		#method for printing object 
		return "Publication: " + str(self.refKey) + ", type: " + str(self.pubType) + ", required fields filled = "+str(self.requiredFieldsFull)\
		 +"\n\t Keywords: " + str(self.keywords)

	def addKeyword(self,keyword):
		#this adds a keyword to a set 
		self.keywords.add(keyword)

	def requiredFieldsCheck(self):
		return False

#Article class inherits from publication 
class Article(Publication):
	"""
	Article class. Inherits from Publication class.
	"""
	pubType = "article"

	#in the overloaded constructor we set all possible fields to empty or None
	def __init__(self,user_key):
		#first we call the base class init
		Publication.__init__(self,user_key)
		##now we initialize the specific attributes
		self.authors = []
		self.authorsCount = 0
		self.title = None
		self.journal = None
		self.journalVolume = None
		self.journalNumber = None
		self.year = None
		self.doi = None
		self.link = None
		self.note = None

	#Required attributes are
	#Author, Title, Journal, Journal volume, Journal number, Publication year
	#Further attributes include 
	#DOI, Link, Keywords, and Notes
	#One author is required but other authors can be added 
	def addAuthor(self,author):
		self.authors.append(author)
		self.authorsCount = len(self.authors)

	def setTitle(self,title):
		self.title = title

	def setJournalName(self,journal):
		self.journalName = journal

	def setJournalVolume(self,volume):
		self.journalVolume = volume

	def setJournalNumber(self,number):
		self.journalNumber = number

	def setYear(self,year):
		self.year = year

	def addDOI(self,doi):
		self.doi = doi

	def addLink(self,link):
		self.link = link

	def addNote(self,note):
		self.note = note

	def requiredFieldsCheck(self):
		#checks if all required fields are full
		#returns result of the check
		#check author count first 
		self.requiredFieldsFull = ( self.authorsCount > 0 ) and\
		 not (None in [self.title,self.journalName,self.journalVolume,self.journalNumber,self.year] )
		return self.requiredFieldsFull
	

#Book class inherits from publication
class Book(Publication):
	"""
	Book class. Inherits from Publication class.
	"""
	pubType = "book"

	#in the overloaded constructor we set all possible fields to empty or None
	def __init__(self,user_key):
		#first we call the base class init
		Publication.__init__(self,user_key)
		##now we initialize the specific attributes
		self.authors = []
		self.authorsCount = 0
		self.title = None
		self.publisher = None
		self.year = None

	#required attributes are 
	#Author, Title, Publisher, Publishing Year
	#Additional attributes are 
	#Link, Keywords, and Notes
	#One author is required but more can be added 
	def addAuthor(self,author):
		self.authors.append(author)
		self.authorsCount = len(self.authors)

	def setTitle(self,title):
		self.title = title

	def setPublisher(self,publisher):
		self.publisher = publisher

	def setYear(self,year):
		self.year = year

	def addLink(self,link):
		self.link = link

	def addNote(self,note):
		self.note = note

	def requiredFieldsCheck(self):
		#checks if all required fields are full
		#returns result of the check
		#check author count first 
		self.requiredFieldsFull = ( self.authorsCount > 0 ) and\
		 not (None in [self.title,self.publisher,self.year] )
		return self.requiredFieldsFull

#Some default debugging instances of the provided classes 
debug_publication = Publication("debug_publication")
debug_publication.addKeyword("Debug")
debug_publication.addKeyword("Publication")
debug_publication.addKeyword("Test")

debug_article = Article("debug_article")
debug_article.addAuthor("First Author")
debug_article.setTitle("The Title")
debug_article.setJournalName("Journal Name")
debug_article.setJournalVolume(500)
debug_article.setJournalNumber(30)
debug_article.setYear(2016)
debug_article.addDOI("DOI")
debug_article.addLink("www.thelink.com")
debug_article.addAuthor("Second Author")
debug_article.addKeyword("debug")
debug_article.addKeyword("article")
debug_article.addKeyword("test")

debug_book = Book("debug_book")
debug_book.addAuthor("First Author")
debug_book.setTitle("The Title")
debug_book.setPublisher("Publisher Name")
debug_book.setYear(2016)
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