#!/usr/bin/python3

class Router:
	'''Router Class *Always start class names with a capitol letter'''
	def __init__(self, model, swversion, ip_add):
		'''initailize values - __name__ is also known as a magic method'''
		self.model = model
		self.swversion = swversion
		self.ip_add = ip_add
	
	def getdesc(self):
		'''Return a formated description of the router'''
		desc = f'Router Model             :{self.model}\n'\
			   f'Software Version         :{self.swversion}\n'\
			   f'Router Management Address:{self.ip_add}'
		return desc

class Switch(Router):
	def getdesc(self):
		'''return a formated description of the router'''
		desc = f'Switch Model             :{self.model}\n'\
			   f'Software Version         :{self.swversion}\n'\
			   f'Switch Management Address:{self.ip_add}'
		return desc