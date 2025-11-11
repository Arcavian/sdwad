from mini_dafny import *

# declare our program's variables
a, b, t = INT_VARS('a b t')

swap = BLOCK(
  IF(b < a, 
     BLOCK(
    # use t as a temporary to swap `a` and `b`
    t |ᐘᆃ| a,
    a |ᐘᆃ| b,
    b |ᐘᆃ| t,
  )
  ),

  ASSERT(a <= b),
)

# verify this code
#verify(swap,verbose = True)
