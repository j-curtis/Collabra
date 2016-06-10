#Collabra 
#Jonathan Curtis, Jun 9 2016 

#this file defines the user interfacing protocols for the Collabra program
#it also defines a user session class and enables basic command line user interfacing
import Objects

#first we define the general class for a user session
class Session(object):
	def __init__(self):
		self.requestQuit = False	#this is always false until the user requests to quit the session. Then it is switched to true
		self.dbFileName=""	#the name of the file holding the database we are mounting for our session
		self.dbFile = None	#the actual file of the current database 
		self.db=None	#the actual database located at dbFileName (the internal representation at least)

	def hasFile(self):
		"""Checks to see if there is a currently mounted file"""
		return not (self.dbFile == None or self.dbFileName == "")
			

	def hasDB(self):
		"""Checks to see if there is a currently defined internal database"""
		return not self.db==None


	def commandUnmount(self):
		"""Closes the currently mounted file without saving. Internal database persists until a new one is opened/cleared"""
		if self.hasFile():
			self.dbFile.close()
			self.dbFile = None
			self.dbFileName = ""

	def commandMount(self,dbFileName):
		"""Mounts the database located at dbFile. Unmounts database first without saving. Does not load database"""
		self.commandUnmount()
		self.dbFileName=dbFileName
		self.dbFile=open(self.dbFileName,'r+')

	def commandSave(self):
		"""Saves the current internal representation of the database to the file currently open"""
		if self.hasFile() and self.hasDB() :
			self.dbFile.write(self.db.toJSONString())

	def commandLoad(self):
		"""Reads in currently mounted file. Replaces current internal database with the contents of the new file."""
		if self.hasFile():
			JSON_string = self.dbFile.read()
			self.db = Objects.Database.fromJSONString(JSON_string)

	def commandClear(self):
		"""Unmounts the current database and deletes the current internal database object"""
		self.commandUnmount()
		self.db = None

	def commandNew(self,dbFileName,dbObjName):
		"""Clears current session.
		Then creates a new file with location dbFileName and creates a database object with objName dbObjName"""
		self.commandClear()
		self.dbFileName = dbFileName
		self.dbFile = open(self.dbFileName,"w")
		self.db = Database(objName=dbObjName)

	def commandQuit(self):
		"""Clears session. Sends a quit request signal."""
		self.Clear()
		self.requestQuit = True

	def commandEdit(self,edit_string):
		"""Performs the edit indicated by the string 'edit_string' on the current database. 
		Edit command parsed by UserInterface.Parser class, PEdit method."""
		if self.hasDB():
			parser = Parser()
			parser.PEdit(db=self.db,text_string=edit_string)

	def viewDataBase(self,view_string):
		"""Returns a string representation of the database with formatting commands (intended for html/css). 
		View options conveyed via input string 'view_string' and parsed by UserInterface.Parser class, PView method."""
		if self.hasDB():
			parser = Parser()
			r_string = parser.PView(db=self.db,text_string=view_string)

		else:
			r_string = parser.PViewErrorString()

		return r_string



#This class handles the parsing from input/output strings to internal commands 
#the PEdit method converts a string edit command into a sequence of database edit methods
#the PView method converts a string view option into a formatting mode and then returns a formatted string representing the database view
#the PSessionInput method converts a session command string into a session command 
#the PSessionOutput method converts a session output string into a formatted string 
class Parse(object):
	def PEdit(self,db,edit_string):
		"""This parses the string edit_string and turns it into a command. It then performs this command on the database db"""

		"""Here we outline how the parsing works. 
		A text string will be an unordered series of whitespace separated tokens of the form
		CMDvalue.
		CMD is a unique three-letter (uppercase) identifier that specifies what edit command is issued.
		'value' is an acceptable value for that command to take (could be empty)
		If the command specified by name is a unary operator, then value will be omitted (so that the token is CMD).
		
		Often, 'value' will be a string. In such a case the string does not need to be escaped.  
		We will use an escape character of ^ (carrot).
		A null character will be ^0
		A space is given by ^1
		A newline is given by ^2 
		A single quote will be ^< for opening and ^> for closing 
		A double quote is two single quotes separated by a null character
		A literal carrot will be ^^
		As an example, the command NAM taking value 'E = mc^2' (including quotes) would be written as 
		NAM^<E^1=^1mc^^2^>
		"""
		
		"""We now summarize the possible commands and their values"""




