#Collabra 
#Jonathan Curtis, June 5, 2016

#This file details the various user interface classes 
import DatabaseClass
import PublicationClass
import sys

class Session:
	"""
	Class for user interfacing with database files.
	"""
	
	def __init__(self):
		#We initialize all attributes to None
		
		#DB management attribute variables 
		self.databaseFilePath = None #the full /path/to/file/name.extension
		self.database = None	#the internal representation of the mounted database 

		#Input/Output variables
		self.input = None	#the current input from the user to the session
		self.output = None 	#the current output from the session to the user (how commands return values to the user)

	
#Classes for session commands
class Command:
	"""
	Class for session commands.
	Each command, when it is called, is passed a session. It acts on this session when it is called.
	Base class is a general command structure and derived classes are specific commands.
	"""
	def __init__(self,session):
		self.session = session 	#the session the command is acting on 
		self.commandName = None	#name of the command called (string)

	#returns the command name as the string representation of the object 
	def __str__(self):
		return self.commandName 

class GetDBName(Command):
	def __init__(self,session):
		Command.__init__(self,session)	#Call the parent constructor first
		self.commandName = "get-db-name"	#the command name for this command 

		#here is where we actually implement the command action 
		self.session.output = self.session.database.name 

class GetDBSize(Command):
	def __init__(self,session):
		Command.__init__(self,session)	#Call the parent constructor first
		self.commandName = "get-db-size"	#the command name for this command 

		#here is where we actually implement the command action 
		self.session.output = self.session.database.entryCount 

class GetDBFilePath(Command):
	def __init__(self,session):
		Command.__init__(self,session)
		self.commandName = "get-db-file-path"

		self.session.output = self.session.databaseFilePath

class Unmount(Command):
	def __init__(self,session):
		Command.__init__(self,session)
		self.commandName = "unmount"

		self.session.output = "Unmounting current database..."
		self.session.database = None 
		self.session.databaseFilePath = None 

class Mount(Command):
	def __init__(self,session,filePath):
		Command.__init__(self,session)
		self.commandName = "mount"

		self.session.output = "Mounting database located at "+filePath+"..."
		self.session.databaseFilePath = filePath #change locations to the new database file 
		self.session.database = 















