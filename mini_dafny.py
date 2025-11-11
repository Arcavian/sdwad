import random
from z3 import *

# hack for custom infix operators
class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(
          lambda x, self=self, other=other: 
            self.function(other, x))
    def __or__(self, other):
        return self.function(other)

ᐘᆃ = Infix(lambda v, e: ASSIGN(v, e))

#*************************************************
 #Insert your code here
def INT_VARS(vs):  
    vars = vs.split()
    if len(vars) == 1:
      return 0
    else:
      return [0 for v in vs.split()]


class Stmt:
  pass

class ASSIGN(Stmt):
   def __init__(self, var, expr):
      pass
   def wp(self, post):
      #Insert code that computes the weakest precondition for ASSIGN
      pass
   
class BLOCK(Stmt):
    def __init__(self, *stmts):
       self.stmts = stmts

#*************************************************

#
# Verifying Programs
#
def verify(stmt, pre = True, post = True, verbose = True):
  vc = Implies(pre, stmt.wp(post))  
  s = Solver()
  s.add(Not(vc))
  r = s.check()
  if verbose:
      print(f'''
-----------------------------------
Verification Condition
-----------------------------------

{vc}

-----------------------------------
Simplified Verification Condition
-----------------------------------

{simplify(vc)}

-----------------------------------
Solver Response
-----------------------------------
      '''.strip())
  s = Solver()
  s.add(Not(vc))
  r = s.check()
  if verbose:
    if r == unsat:
      print("proved!")
    elif r == unknown:
      print("failed to prove")
      print(s.model())
    else:
      print("counterexample")
      print(s.model())
    print()
  return r