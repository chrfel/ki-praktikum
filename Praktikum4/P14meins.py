from nltk.sem.logic import *
from nltk import *
from nltk.tree import *
from nltk.draw import *

lgp = LogicParser()
e1 = lgp.parse(r'( ( A | B | C ) & ( A | B | -C ) & ( -A | B | C ) & ( -A | -B | C ) )')
tree = Tree.fromstring(str(e1))
tree.draw()
