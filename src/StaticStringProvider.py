#from . import IStringProvider # when we were in ioUtils folder, this was right
import IStringProvider

class StaticStringProvider(IStringProvider.IStringProvider):
	"""docstring for StaticStringProvider"""
	def __init__(self, text):
		super(StaticStringProvider, self).__init__()
		self.text = text

	def provide(self):
		return self.text