from mini_dafny import *

# We want to verify Hoare conditional rule
#  if x > y 
#    y := x
#  assert y >= x

# declare variables
x, y = INT_VARS('x y')

# code to verify
if_2 = BLOCK(
  ASSUME(x >= 0),
  IF(x > y , BLOCK(
      y |ᐘᆃ| x
    )),
  ASSERT(y >= x),
)

# verify this code
verify(if_2,verbose = True)
