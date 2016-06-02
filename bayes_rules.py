######################################
#         Bayes Rules                #
######################################

"""
p(c) = 0.1 p(nC) = 0.9
p(pos|c) = 0.9 p(neg|c) = 0.1
p(neg|nc) = 0.5 p(pos|nc) = 0.5

p(c,pos) = 0.1*0.9=0.09
p(nc,pos) = 0.9*0.5 = 0.45
p(pos) = 0.09 + 0.45 = 0.54
p(c|pos) = 0.166667
p(nc|pos) = 0.83333

p(r) = 0.5  p(g) = 0.5
p(see r|at r) = 0.8 p(see g|at r) = 0.2
p(see g|at g) = 0.8 p(see r|at g) = 0.2

p(at r, see r) = 0.4
p(at g, see r) = 0.1
p(see r) = 0.5
p(at r|see r) = 0.8
p(at g|see r) = 0.2


p(r) = 0.5  p(g) = 0.5
p(see r|at r) = 0.8 p(see g|at r) = 0.2
p(see g|at g) = 0.5 p(see r|at g) = 0.5

p(at r, see r) = 0.40
p(at g, see r) = 0.25
p(see r) = 0.65
p(at r|see r) = 0.62
p(at g|see r) = 0.38
"""
