#Collabra 
#Jonathan Curtis, June 5, 2016

#This file is the class file for the command-line user interface 
import DatabaseClass
import PublicationClass

#this class handles user interfacing through the command line 
#an instance of this class is known as a 'session'
#in a session, the user can issue commands
#each session may have up to one database active at once
#when a database (DB) is under the scope of the session, it is 'mounted'
class CommandLineSession:
	"""
	Class for interfacing with database(s) through the command line.
	"""
	
	def __init__(self):
		#We initialize all attributes to None
		
		#DB management
		self.databaseName = None	#the name of the current mounted database 
		self.databaseFilePath = None #the full /path/to/file/name.extension
		self.database = None	#the internal representation of the mounted database 

	#USER COMMANDS 
	##DB management commands

	###Returns the name of the mounted DB 
	def commandDBGetName(self):
		return self.databaseName

	###Returns the location of the mounted DB
	def commandDBGetFilePath(self):
		return self.databaseLocation

	###Unmounts the current database 
	###It does NOT save the DB before unmounting it 
	def commandDBUnmount(self):
		self.database = None
		self.databaseName = None 
		self.databaseFilePath = None 

	###Mounts the database whose location is passed 
	###If there is a database currently mounted, that one is unmounted (and is NOT saved)
	def commandDBMount(self,databaseFilePath):
		#Unmount any currently mounted databases
		self.commandDBUnmount()















