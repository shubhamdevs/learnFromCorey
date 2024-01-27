# to import a module we write: import <module-name>
# by importing we can get all access to the functions and cod3e of the impoting module
import math
print(math.pi)

# we can import a module and give it a custom alias
import random as rand
# now we can call the function by pd

# if we want to import a single item from a module
from math import pi

# we can import several variable from a module by coma separation

# we can shorthand the importing variables
from math import pi as p

# now we are giving pi variable/function a custom alias as p

# if we want to import everything, we use
from math import *

import sys
print(sys.path)
