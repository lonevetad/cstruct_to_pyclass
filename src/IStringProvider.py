class IStringProvider(object):
	"""docstring for IStringProvider"""
	def __init__(self):
		super(IStringProvider, self).__init__()
	
	def provide(self):
		raise NotImplementedError
