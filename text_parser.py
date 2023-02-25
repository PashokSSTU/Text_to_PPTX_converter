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

		# Проверка на наличие разбиение текста на фрагменты для слайдов.
		# Если после разделительного символа стоит enter - то удаляем его.
		if self.slides > 1:

			# КОСТЫЛЬ. Обходим список строк с конца до тех пор, пока не встретим не пустую строку. 
			# Пустые строки в процессе обхода удаляем.
			while True:
				if self.text[-1] == '':
					self.text.pop(-1)
					self.slides -= 1
				else:
					break

			text_str_index = 0

			while text_str_index < len(self.text):
				self.text[text_str_index] = list(self.text[text_str_index])

				if len(self.text[text_str_index]) == 0:
					self.slides -= 1 						# Уменьшаем количество слайдов, если встретили пустую строку.
					self.text.pop(text_str_index) 			# Удалаем пустую строку.
				elif len(self.text[text_str_index]) > 0 and self.text[text_str_index][0] == "\n":
					self.text[text_str_index][0] = "" 		# Удаляем enter.
					self.text[text_str_index] = "".join(self.text[text_str_index])

				text_str_index += 1


		return ["".join(slide) for slide in self.text] # Конвертируем внутри многомерного списка списки символов в списки строк
													   # и возвращаем многомерный список.

	def amounthOfSlides(self):
		return self.slides