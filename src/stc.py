from StaticStringProvider import *
from FileStringProvider import *
from InputToModel import *

grammarProvider = FileStringProvider("../configs/grammar.txt")

def main():
	print(grammarProvider.provide())

def folder_output_from_input(input_file, inputType):
	out_folder = "./"
	if inputType == "f":
		o = out_folder
		folder_term = input_file.rfind("/")
		if folder_term < 0:
			folder_term = input_file.rfind("\\")
		if folder_term > 1:
			o = input_file[0:folder_term+1]
		if len(o) > 0:
			out_folder = o
	return out_folder

def convert(inputs, inputType = None ):
	itm = InputToModel(grammarProvider)
	if inputType == None:
		inputType = "f"
	is_string = (inputType == "s")
	for i in inputs:
		ip = None
		
		if is_string:
			ip = StaticStringProvider(i)
		else:
			ip = FileStringProvider(i)
		model = itm.to_model(ip)
		
		# TODO define the model_to_output and the "outputter"

		folder_output = folder_output_from_input(i, inputType)
		print(folder_output)

	



if __name__ == '__main__':
	main()
	print("EHEHHEEHHEEHHEHEH")
	convert(["./single.txt", "./double.txt", "./multiple.txt", "./arrays.txt", "./404/lel.txt"])
