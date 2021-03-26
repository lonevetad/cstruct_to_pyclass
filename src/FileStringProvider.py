#from . import IStringProvider # when we were in ioUtils folder, this was right
import IStringProvider

class FileStringProvider(IStringProvider.IStringProvider):
	"""docstring for FileStringProvider"""
	def __init__(self, urlFile):
		super(FileStringProvider, self).__init__()
		self.urlFile = urlFile

	def provide(self):
		text_file = open(self.urlFile, "r")
 		#read whole file to a string
		data = text_file.read()
		#close file
		text_file.close()
		return data