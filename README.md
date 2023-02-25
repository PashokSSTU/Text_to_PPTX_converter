# Text_to_PPTX_converter

## Список сторонних библиотек
* [cx_Freeze](https://pypi.org/project/cx-Freeze/) - для сборки исполняемого файла со всеми зависимостями.
* (В НАСТОЯЩИЙ МОМЕНТ НЕ ПОДДЕРЖИВАЕТСЯ!)[pyinstaller](https://pypi.org/project/pyinstaller/) - для сборки единого исполняемого файла
* [PyQT5](https://pypi.org/project/PyQt5/) - для создания dekstop приложения.
* [python-pptx](https://pypi.org/project/python-pptx/) - для работы с файлами .pptx для презентация Microsoft Power Point.
* [python-docx](https://pypi.org/project/python-docx/) - для работы с docx файлами Microsoft Word.
* [pywin32](https://pypi.org/project/pywin32/) -  - для работы с doc файлами Microsoft Word.

## Инструкции к сборке приложения

### Windows
#### Сборка с помощью cx_Freeze
Откройте терминал.
Введите туда следующие команды:
```
cd {путь_к_директории_со_скриптом_setup.py}
python setup.py build
```
После этого у вас создастся директория build, в которой должна будет лежать папка с собранным исполняемым файлом и с необходимыми зависимостями.

#### Сборка с помощью pyinstaller (В НАСТОЯЩИЙ МОМЕНТ НЕ ПОДДЕРЖИВАЕТСЯ!)
Откройте терминал.
Введите туда следующие команды:
```
cd {путь_к_директории_со_скриптом_setup.py}
pyinstaller --name={nameApp} --onefile {main_script}.py
```
После этого должна создасться директория dist с единым исполняемым файлом.