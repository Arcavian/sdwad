from mini_dafny import *

# We want to verify Hoare assignment rule
#  assume x >= 0
#  x := x + 1
#  assert x >= 1
#


# declare variables
x = INT_VARS('x')

# code to verify
asgn = BLOCK(
  ASSUME(x >= 0),
  x |ᐘᆃ|  x  + 1,
  ASSERT(x >= 1),
)

# verify this code
verify(asgn,verbose = True)
