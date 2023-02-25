import os
import docx
import win32com.client
import re

class TextReader:

	def __init__(self, path, textDelimiter):
		self.path_to_file = path
		self.text_delimiter = textDelimiter
		self.text = None
		self.slides = None

	def read(self):
		if os.path.splitext(self.path_to_file)[1] != ".doc" and os.path.splitext(self.path_to_file)[1] != ".docx":
			with open(self.path_to_file, "r", encoding="utf-8") as f:
				self.text = f.read()
		elif os.path.splitext(self.path_to_file)[1] == ".docx":
			doc = docx.Document(self.path_to_file)
			self.text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
		elif os.path.splitext(self.path_to_file)[1] == ".doc":
			word = win32com.client.Dispatch("Word.Application") # Создаем COM-объект приложения Microsoft Word
			doc = word.Documents.Open(self.path_to_file) # Открываем файл для чтения
			self.text = doc.Content.Text # Считываем содержимое документа
			doc.Close() # Закрываем файл
			word.Quit() # Закрываем приложение Word

		# Заменяем все вхождения символов новой строки и переноса каретки на пустую строку с помощью регулярных выражений
		self.text = re.sub(r'[\n\r]+', '\n', self.text)
		self.text = self.text.split(self.text_delimiter)
		self.slides = len(self.text)

		# Проверка на наличие разбиение текста на фрагменты для слайдов.
		# Если после разделительного символа стоит enter - то удаляем его. ВАЖНО: удаляется только один enter!
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