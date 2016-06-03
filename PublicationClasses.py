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

#Article class inherits from this 
class Article(Publication):
	"""
	Article class. Inherits from Publication class.
	"""
	pubType = "article"

	#Required article attributes 
	#(First) Author, Title, Journal, Journal volume, Journal number, Publication year
	#Further options include 
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

	print pub0
	print
	print pub1
	print

if __name__ == "__main__":
	main()