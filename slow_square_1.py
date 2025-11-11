from mini_dafny import *

# We want to verify Hoare skip rule. 
#  assume n >= 0
#  a := 0
#  i := 0
#  while i < n
#  invariant a == n * i
#  {
#     i := i + 1
#     a := a + n
#  }
#  assert (a == n * n)

# Above program does not verify because the invariant does not guarantee i <=n when the loop terminates. 

# declare our program's variables
a, i, n = INT_VARS('a i n')

# code that we would like to verify
# in this case, it computes n * n by iterative addition
code = BLOCK(
  ASSUME(0 <= n),

  a |ᐘᆃ| 0,
  i |ᐘᆃ| 0,

  WHILE(i < n,
    # invariant
    #TRUE.smt_encode(),
    AND(a == n * i).smt_encode(),

    # body
    i |ᐘᆃ| i + 1,
    a |ᐘᆃ| a + n,
  ),
  ASSERT(a == n * n),
)

# ask the solver to check this code
verify(code)
