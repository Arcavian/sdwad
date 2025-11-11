from mini_dafny import *

# We want to verify Hoare skip rule. 
#  assume x >= 0
#  skip()
#  assert x == 0
#
#Of course, this code does not verify.

# declare our program's variables
x = INT_VARS('x')

skip = BLOCK(
  ASSUME(x >= 0),
  SKIP(),
  ASSERT(x == 0),
)

# verify this code
verify(skip,verbose = True)
