import sys


from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
options = {
    'build_exe': {
            'packages': ['scipy'], # 重要
            'includes': ['atexit',
                         'numpy',
                         'scipy','matplotlib.backends.backend_tkagg', 'tkinter.filedialog','tkinter','os','numpy.core._methods', 'numpy.lib.format',],
            'excludes': ['Tkinter',
                         'collections.sys',
                         'collections._weakref']
    }
}

setup(
        name="test",
        version="1.0",
        description="",
        options=options,
        executables=[Executable("E:\\code\\PRML辅助教学系统\\main.py", base=base,icon="cartoon1.ico")])