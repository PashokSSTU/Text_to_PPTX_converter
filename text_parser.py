class TextReader:

	def __init__(self, path, textDelimiter):
		self.path_to_file = path
		self.text_delimiter = textDelimiter
		self.text = None
		self.slides = None

	def read(self):
		with open(self.path_to_file, "r", encoding="utf-8") as f:
			self.text = f.read()
		
		self.text = self.text.split(self.text_delimiter)
		self.slides = len(self.text)

		return self.text

	def amounthOfSlides(self):
		return self.slides



