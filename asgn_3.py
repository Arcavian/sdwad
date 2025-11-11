from mini_dafny import *

# We want to verify Hoare assignment rule
#  assume 2 * (x + 3) >= 6
#  x := x + 3
#  x := x * 2
#  assert x >= 6

# declare variables
x = INT_VARS('x')

# code to verify
asgn = BLOCK(
  ASSUME((x+3) * 2 >= 6),
  x |ᐘᆃ|  x + 3,
  x |ᐘᆃ|  x * 2,
  ASSERT(x >= 6),
)

# verify this code
verify(asgn,verbose = True)
