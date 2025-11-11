from mini_dafny import *

# declare our program's variables
a, b, t = INT_VARS('a b t')

code = BLOCK(
    t |ᐘᆃ| a,
    a |ᐘᆃ| b,
    b |ᐘᆃ| t,
    ASSERT(a == b)
)

# verify this code
verify(code,verbose = True)
