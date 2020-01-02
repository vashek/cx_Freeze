# A setup script to demonstrate the use o pytz
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

setup(name='test_pytz',
      version='0.1',
      description='cx_Freeze script to test pytz',
      executables=[Executable("test_pytz.py")],
      options={'build_exe': {'zip_include_packages': ["*"],
                             'zip_exclude_packages': []}})