import sys
def py2_or_py3():
    major=sys.version_info.major
    if (major==2):
        print("Python 2")
    else:
        print("Python 3 System")
py2_or_py3()