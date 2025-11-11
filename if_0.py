from mini_dafny import *

# We want to verify Hoare conditional rule
#  if x > 0 
#    y := x
#  else
#    y := 1  
#  assert y > 0


# declare variables
x, y = INT_VARS('x y')

# code to verify
if_0 = BLOCK(
  IF(x > 0 , BLOCK(
      y |ᐘᆃ| x
    ),
  (BLOCK(
      y |ᐘᆃ| 1
    )
  )),
  ASSERT(y > 0),
)

# verify this code
verify(if_0,verbose = True)
