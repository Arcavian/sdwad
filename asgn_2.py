from mini_dafny import *

# We want to verify Hoare assignment rule
#  assume i >= j
#  i := i + 1
#  j := j + 1
#  assert i >= j


# declare variables
i,j = INT_VARS('i j')

# code to verify
asgn = BLOCK(
  ASSUME(i > j),
  i |ᐘᆃ|  i  + 1,
  j |ᐘᆃ|  j  + 1,
  ASSERT(i > j+1),
)

# verify this code
verify(asgn,verbose = True)
