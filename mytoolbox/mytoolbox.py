""" This module has the same name as the package
"""

# Problematic import
from mytoolbox import mymodule1

# This works
# from mytoolbox.mymodule1 import (myTypeAlias,
#                                 myTypeVar,
#                                 myClass1,
#                                 myGlobalFunction,
#                                 myError)

class MyToolBoxClass():
    """
    A class inside the module having the package's name
    """
    pass
