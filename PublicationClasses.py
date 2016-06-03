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
		self.refKey = user_key 
		self.keywords = []	#all publications can have keywords 

	def __str__(self):
		#method for printing object 
		return str(self.refKey) + ": " + str(self.pubType) + ".\n\t Keywords = " + str(self.keywords)

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
	def setAuthor(self,author):
		self.authors = []
		self.authors.append(author)

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

	def addKeyword(self,keyword):
		self.keywords.append(keyword)

	def addNote(self,note):
		self.note = note

	def addAuthor(self,author):
		self.authors.append(author)

#Book class inherits from publication
class Book(Publication):
	"""
	Book class. Inherits from Publication class.
	"""
	pubType = "book"

	#required attributes are 
	#Author, Title, Publisher, Publishing Location, Publishing Year
	#Additional attributes are 
	#Link, Keywords, and Notes
	#One author is required but more can be added 

	def setAuthor(self,author):
		self.authors = []
		self.authors.append(author)

	def setTitle(self,title):
		self.title = title

	def setPublisher(self,publisher):
		self.publisher = publisher

	def setLocation(self,location):
		self.location = location

	def setYear(self,year):
		self.year = year

	def addLink(self,link):
		self.link = link

	def addKeyword(self,keyword):
		self.keywords.append(keyword)

	def addNote(self,note):
		self.note = note

	def addAuthor(self,author):
		self.authors.append(author)


def main():
	#debugging 
	pub0 = Publication("no_pub")

	pub1 = Article("myFirstPub")
	pub1.setAuthor("Jon Curtis")
	pub1.setTitle("My First Publication")
	pub1.setJournalName("Physical Review Letters")
	pub1.setJournalVolume("40")
	pub1.setJournalNumber("52")
	pub1.setYear("2016")
	pub1.addKeyword("First")
	pub1.addKeyword("Publication")
	pub1.addAuthor("J.B. Curtis")

	pub2 = Book("myFirstBook")
	pub2.setAuthor("Jon Curtis")
	pub2.setTitle("Book Writing For Dummies")
	pub2.setPublisher("Publishing Company")
	pub2.setLocation("New York City")
	pub2.setYear("2020")
	pub2.addKeyword("Publishing")
	pub2.addKeyword("Dummies")
	pub2.addAuthor("Your Mom")


	print pub0
	print
	print pub1
	print
	print pub2
	print pub2.authors

if __name__ == "__main__":
	main()