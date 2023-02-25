from cx_Freeze import setup, Executable

setup(name='Text to pptx converter',
      version='0.2.0',
      description='This is converter text to microsoft Power Point presentation.',
      executables=[Executable('Application.py', base="Win32GUI")])