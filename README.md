# PathDoctor

Finds copies of Python inside and outside of the Windows Path.

Written to help troubleshoot new user problems on [Python Discord](https://pythondiscord.com).

## Quick Run
If you can run Python from a cmd window, try copy-pasting this. Otherwise, download an exe from [releases](https://github.com/thillsd/pathdoctor/releases).

```
python -c "import urllib.request; exec(urllib.request.urlopen(r'https://raw.githubusercontent.com/thillsd/pathdoctor/main/pathdoctor/pathdoctor.py').read())"
```

## Example Output
```python
PythonInstallation(directory='C:\Users\t\Desktop\projects\pathdoctor\.venv\Scripts',
                   interpreter='C:\Users\t\Desktop\projects\pathdoctor\.venv\Scripts\python.exe',
                   python_in_path=True,
                   pip='C:\Users\t\Desktop\projects\pathdoctor\.venv\Scripts\pip.exe',
                   pip_in_path=True,
                   is_default_interpreter_in_path=True,
                   is_the_currently_running_interpreter=True)
PythonInstallation(directory='C:\Python311',
                   interpreter='C:\Python311\python.exe',
                   python_in_path=True,
                   pip='C:\Python311\Scripts\pip.exe',
                   pip_in_path=True,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
PythonInstallation(directory='C:\msys64\mingw64\bin',
                   interpreter='C:\msys64\mingw64\bin\python.exe',
                   python_in_path=True,
                   pip=None,
                   pip_in_path=False,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
PythonInstallation(directory='C:\Users\t\AppData\Local\Programs\Python\Python312-32',
                   interpreter='C:\Users\t\AppData\Local\Programs\Python\Python312-32\python.exe',
                   python_in_path=False,
                   pip='C:\Users\t\AppData\Local\Programs\Python\Python312-32\Scripts\pip.exe',
                   pip_in_path=False,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
PythonInstallation(directory='C:\Users\t\AppData\Local\Programs\Python\Python38',
                   interpreter='C:\Users\t\AppData\Local\Programs\Python\Python38\python.exe',
                   python_in_path=False,
                   pip='C:\Users\t\AppData\Local\Programs\Python\Python38\Scripts\pip.exe',
                   pip_in_path=False,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
PythonInstallation(directory='C:\ProgramData\anaconda3',
                   interpreter='C:\ProgramData\anaconda3\python.exe',
                   python_in_path=False,
                   pip='C:\ProgramData\anaconda3\Scripts\pip.exe',
                   pip_in_path=False,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
PythonInstallation(directory='C:\Users\t\miniconda3',
                   interpreter='C:\Users\t\miniconda3\python.exe',
                   python_in_path=False,
                   pip='C:\Users\t\miniconda3\Scripts\pip.exe',
                   pip_in_path=False,
                   is_default_interpreter_in_path=False,
                   is_the_currently_running_interpreter=False)
