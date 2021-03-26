from textx import metamodel_from_str

class InputToModel(object):
	"""docstring for InputToModel"""
	def __init__(self, grammarProvider):
		super(InputToModel, self).__init__()
		self.meta_model = metamodel_from_str(grammarProvider.provide())
	
	def get_metamodel(self):
		return self.meta_model

	def to_model(self, inputPovider):
		return self.meta_model.model_from_str(inputPovider.provide())
	