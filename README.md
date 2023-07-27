# PythonPathDoctor

Finds copies of Python inside and outside of the Windows Path.

```python
PythonInstallation(directory='C:\Users\t\Desktop\projects\pythonpathdoctor\.venv\Scripts',
                   interpreter='C:\Users\t\Desktop\projects\pythonpathdoctor\.venv\Scripts\python.exe',
                   python_in_path=True,
                   pip='C:\Users\t\Desktop\projects\pythonpathdoctor\.venv\Scripts\pip.exe',
                   pip_in_path=True,
                   is_current_interpreter=True)
PythonInstallation(directory='C:\Python311',
                   interpreter='C:\Python311\python.exe',
                   python_in_path=True,
                   pip='C:\Python311\Scripts\pip.exe',
                   pip_in_path=True,
                   is_current_interpreter=False)
PythonInstallation(directory='C:\msys64\mingw64\bin',
                   interpreter='C:\msys64\mingw64\bin\python.exe',
                   python_in_path=True,
                   pip=None,
                   pip_in_path=False,
                   is_current_interpreter=False)
PythonInstallation(directory='C:\Users\t\AppData\Local\Programs\Python\Python312-32',
                   interpreter='C:\Users\t\AppData\Local\Programs\Python\Python312-32\python.exe',
                   python_in_path=False,
                   pip='C:\Users\t\AppData\Local\Programs\Python\Python312-32\Scripts\pip.exe',
                   pip_in_path=False,
                   is_current_interpreter=False)
PythonInstallation(directory='C:\Users\t\AppData\Local\Programs\Python\Python38',
                   interpreter='C:\Users\t\AppData\Local\Programs\Python\Python38\python.exe',
                   python_in_path=False,
                   pip='C:\Users\t\AppData\Local\Programs\Python\Python38\Scripts\pip.exe',
                   pip_in_path=False,
                   is_current_interpreter=False)
```

Link to releases.

Quick run:

Save and run a copy of 

```
python -c "import urllib.request; exec(urllib.request.urlopen(r'https://raw.githubusercontent.com/dbarnett/python-helloworld/master/helloworld.py').read())"
```