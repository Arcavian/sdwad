from mini_dafny import *

# We want to verify Hoare while rule. 

  # var n := a;
  # assume{:axiom}{:axiom} n > 0;
  # var i := n;
  # assert i <= n;
  # while (i > 0)
  #   invariant i <= n
  # {
  #   i := i - 1;
  # }
  # assert i == 0;
  
# declare variables
i,n = INT_VARS('i n')

# code to verify
code = BLOCK(
  ASSUME(0 < n),
  i |ᐘᆃ| n,
  WHILE(0 < i,
    # invariant
    AND(i <= n, i >=0).smt_encode(),
    
    # body
    i |ᐘᆃ| i - 1,
  ),
  ASSERT(i > 0),
)

# ask the solver to check this code
#verify(code, verbose = True)
