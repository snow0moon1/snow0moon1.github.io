from pymprog import *
begin('bike production')
A, B = var('A, B') # variables
maximize(200000 * A + 80000 * B, 'profit')
3000*A + 900*B <= 75000 # mountain bike limit
5*A >= 5 # racer production limit
1*A <= 15

solve()