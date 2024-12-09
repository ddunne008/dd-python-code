import sympy as fac

def calc_factors(n):
    factors = fac.factorint(n)
    return factors

print(calc_factors(28))