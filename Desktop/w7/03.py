from pulp import *

prob = LpProblem("Textile", LpMinimize)

# 變數
C_30= LpVariable("C_30", lowBound=0, cat='Integer')
C_92= LpVariable("C_92", lowBound=0, cat='Integer')
D_21= LpVariable("D_21", lowBound=0, cat='Integer')
E_11= LpVariable("E_11", lowBound=0, cat='Integer')

# 目標
prob += 0.12*C_30 + 0.09* C_92+ 0.11*D_21+0.04*E_11

# 限制
prob += 1 *C_30+1*C_92>=50*0.45
prob += 1 *E_11>=50*0.15
prob += 1 *D_21+1*C_92<=50*0.3
prob += 1*C_30 + 1* C_92+ 1*D_21+1*E_11>=50

# 解算
prob.writeLP("Textile.lp")
prob.solve()

if prob.status == 1:
    
#     解答物件

    for i in prob.variables():
        if i.name == 'C_30':
            C_30= i
        elif i.name == 'C_92':
            C_92 = i
        elif i.name == 'D_21':
            D_21 = i
        elif i.name == 'E_11':
            E_11 = i

    print ("C_30=%d\nC_92=%d\nD_21=%d\nE11=%d\n ANS=%.1f" %
        (C_30.varValue,C_92.varValue,D_21.varValue,E_11.varValue,
         value(prob.objective)))

else:
    print ("FAIL")