# Text_to_PPTX_converter

## Список сторонних библиотек
* [cx_Freeze](https://pypi.org/project/cx-Freeze/) - для сборки исполняемого файла со всеми зависимостями.
* [PyQT5](https://pypi.org/project/PyQt5/) - для создания dekstop приложения.
* [python-pptx](https://pypi.org/project/python-pptx/) - для работы с файлами .pptx для презентация Microsoft Power Point.

## Инструкции к сборке приложения

### Windows
Для создания директории build откройте терминал.
Введите туда следующие команды:
```
cd {путь_к_директории_со_скриптом_setup.py}
python setup.py build
```
После этого у вас создастся директория build, в которой должна будет лежать папка с собранным исполняемым файлом и с необходимыми зависимостями.