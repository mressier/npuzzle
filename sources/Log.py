import sys

class Log:

	filename = "soluce.txt"

	def __init__(self):
		self.out = sys.stdout
		self.err = sys.stderr
		self.verbose = False
		self.out_file = None

	def __del__(self):
		if self.out_file:
			self.out_file.close()

	def error(self, string):
		try:
			self.err.write("ERROR: " + str(string) + "\n")
		except:
			return
		
	def warning(self, string):
		try:
			self.err.write("WARNING: " + str(string) + "\n")
		except:
			return

	def default(self, string):
		try:
			self.out.write(str(string) + "\n")
		except:
			return

	def file(self, string):
		if self.out_file is None:
			try:
				self.out_file = open("soluce.txt","w")
			except:
				self.warning("The soluce file is not available")
				self.out_file = None

		if self.out_file:
			try:
				self.out_file.write(string)
			except:
				self.error("Cannot write to the soluce file")

	def debug(self, string):
		if self.verbose:
			self.default(string)

log = Log()
