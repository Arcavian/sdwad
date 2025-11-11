from mini_dafny import *

# We want to verify Hoare conditional rule
# {
#     if a >= b {
#         m := a;
#     }else{
#         m := b;
#     }
#     if c >= m {
#          m := c +1;
#     }
# }
# ensures m >= a && m >= b && m >= c


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
  IF(c > m , BLOCK(
      m |ᐘᆃ| c +1
    )),
  ASSERT(AND(m >= a, m >= b, m >= c)),
  #ASSERT(OR(m ==a, m == b, m ==c)) # if we remove this postcondition, the above program verifies. 
)

# verify this code
verify(code,verbose = True)
