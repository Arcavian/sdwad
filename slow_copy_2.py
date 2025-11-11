from mini_dafny import *

# We want to verify Hoare while rule. 
#var x,y,inp,out
#assume (0 <= inp),
#x := inp;
#y := 0;
#while 0 < x
#invariant x >=0 && y + x  == inp
#{
#    x := x - 1,
#    y := y + 2,
#}
#out := y,
#assert (out == inp),

# declare variables
x, y, inp, out = INT_VARS('x y inp out')

# code to verify
code = BLOCK(
  ASSUME(0 <= inp),
  x |ᐘᆃ| inp,
  y |ᐘᆃ| 0,
  
  WHILE(0 < x,
    # invariant
    AND(x >=0, y + x  == inp).smt_encode(),
    
    # body
    x |ᐘᆃ| x - 1,
    y |ᐘᆃ| y + 2,
  ),
  out |ᐘᆃ| y,
  ASSERT(out == inp),
)

# ask the solver to check this code
verify(code, verbose = True)
