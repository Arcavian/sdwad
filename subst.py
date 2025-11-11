# substitution example
# Z3 provides a substitution function. We can replace a variable with an expression using this substitution function. 
# This is not part of the project. You do not have to do anything in this file.

from z3 import *

x, y = Bools('x y')
expr = And(x, Or(y, And(x, y)))
print(expr)
#And(x, Or(y, And(x, y)))

expr2 = substitute(expr, (x, BoolVal(True)))
print(expr2)
#And(True, Or(y, And(True, y)))
print (simplify(expr2))
#y

a,b = Ints('a b')
expr3  = a * 2 + b * 3
print(expr3)
# a * 2 + b * 3
expr4 = substitute(expr3, (a, (b + 4)))
print(expr4)
# expr4 = (b + 4) * 2 + b *3