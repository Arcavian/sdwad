from mini_dafny import *

# We want to verify Hoare conditional rule
#  if x > 0 
#    y := x
#  else
#    y := 0 
#  assert y > 0

# above codo does not verify


# declare variables
x, y = INT_VARS('x y')

# code to verify
if_1 = BLOCK(
  ASSUME(x >= 0),
  IF(x > 0 , BLOCK(
      y |ᐘᆃ| x
    ),
  (BLOCK(
      y |ᐘᆃ| 0
    )
    )),
  ASSERT(y > 0),
)

# verify this code
verify(if_1,verbose = True)
