from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx
from decimal import *
import codejam.utils.polynomials as pol

class Dynam(object):pass

def solver(data):

    small, large = pol.solve_quadratic(Decimal(2), Decimal((2* data.inner_rad) -1), Decimal(-1 * data.paint_vol))
    #print 'small %s' % small
    #print 'large %s' % large
    return int(large)

def data_builder(f):

    data = Dynam()
    
    data.inner_rad, data.paint_vol = f.get_ints()
    data.inner_rad = Decimal(data.inner_rad)
    data.paint_vol = Decimal(data.paint_vol)

    return data

##def test():
##
##    assert calc_area(6,0) == 21
##    assert calc_area(6,1) == 21
##    assert calc_area(6,3) == 18
##    assert calc_area(4,1) == 10
##    assert calc_area(8,3) == 33
##    assert calc_area(707106780,1) <= 1000000000000000000
##    assert calc_area(707106791,1) >= 1000000000000000000
##    
##    
##
##test()

cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "A", problem_size='large-practice')
