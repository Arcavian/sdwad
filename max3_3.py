from mini_dafny import *

# We want to verify Hoare conditional rule
# {
#     if a >= b {
#         m := a;
#     }else{
#         m := b;
#     }
#     This program does not consider c. It does not verify. 
# }
# ensures m >= a && m >= b && m >= c
# ensures m ==a || m == b || m ==c

# declare variables
a,b,c,m = INT_VARS('a b c m')

# code to verify
code = BLOCK(
  IF(a >= b, 
     BLOCK(
      m |ᐘᆃ| a
    ),
    (BLOCK(
      m |ᐘᆃ| b
    )
    )),
  ASSERT(AND(m >= a, m >= b, m >= c)),
  ASSERT(OR(m ==a, m == b, m ==c)) 
)

# verify this code
verify(code,verbose = True)
