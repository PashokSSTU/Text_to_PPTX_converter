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

		# Проверка на наличие разбиение текста на фрагменты для слайдов
		try:
			if self.slides > 1:
				for text_str_index in range(len(self.text)):
					self.text[text_str_index] = list(self.text[text_str_index])
					self.text[text_str_index][0] = ""
					self.text[text_str_index] = "".join(self.text[text_str_index])

		except Exception as e:
		    print(e)

		return self.text

	def amounthOfSlides(self):
		return self.slides



