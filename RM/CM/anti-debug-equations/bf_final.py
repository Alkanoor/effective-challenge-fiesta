from z3 import *

def get_models(F):
    result = []
    s = Solver()
    s.add(F)
    while True:
        if s.check() == sat:
            m = s.model()
            result.append(m)
            block = []
            for d in m:
                if d.arity() > 0:
                    raise Z3Exception("uninterpreted functions are not supported")
                c = d()
                if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                    raise Z3Exception("arrays and uninterpreted sorts are not supported")
                block.append(c != m[d])
            s.add(Or(block))
        else:
            return result

def verify(v12):
    v17 = z3.BitVec('v17',32)
    v7 = z3.BitVecVal(3,4)
    v6 = (v12&0xff) - ((v12>>8)&0xff)
    v5 = (v12&0xff) - ((v12>>16)&0xff)
    v10 = ((v12>>16)&0xff) - ((v12>>24)&0xff)

    r1 = 2*v7+((v12>>16)&0xff)-2*v5+v6*v7-((v12>>24)&0xff)+1
    a = If(r1 != 0, z3.BitVecVal(1,1), z3.BitVecVal(0,1))

    r2 = 222*v5+51*v6-((v12>>16)&0xff)+((v12>>24)&0xff)
    a += If(r2 != -8985, z3.BitVecVal(1,1), z3.BitVecVal(0,1))

    r3 = 100*v10-v5-22*v6
    a += If(r3 != 1550, z3.BitVecVal(1,1), z3.BitVecVal(0,1))

    v6 = ((v12>>32)&0xff)
    v17 = (v6 >> 7) * 1341

    v6 = ~(v6&255) & 0x7F ^ 0x4C
    v17 += v6 + 700

    v6 = ((v12>>40)&0xff)
    v17 += ((~(v6&255) ^ 0x9B)&255) -700

    v6 = ((v12>>64)&0xff) + 2

    v5 = ((v12>>56)&0xff)
    v10 = ((v12>>48)&0xff)
    v17 += (v6 ^ 0x22 | v10 ^ 0x36 | v5 ^ 0x65) * 1670

    return And(v17 >= -2, (~(2*(v12&0xff)))&255 == 89, v17+a == 0)

if __name__ == "__main__":
    v12 = BitVec("v12", 8*9)

    print(get_models(verify(v12)))
