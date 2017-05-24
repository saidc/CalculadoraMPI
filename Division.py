#Division

from decimal import localcontext, Decimal
from mpi4py import MPI
import sys

Num1 = int( sys.argv[1])
Num2 = int( sys.argv[2])


def Division(num1, num2):
    with localcontext() as ctx:
        ctx.prec = 10   
        c = Decimal(num1) / Decimal(num2)
    return float(c)
print(Division(Num1,Num2))
