from pymprog import *
begin('bike production')
A, B = var('A, B') # variables
minimize(0.10 * A + 0.15 * B, 'profit')
5*A + 10*B >= 45 # mountain bike limit
4*A + 3*B >=24 # racer production limit
0.5*A >= 1.5
A,B >= 0 # metal finishing limit
solve()