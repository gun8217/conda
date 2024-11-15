def andGate(x1, x2):
    w1, w2, b = 1, 1, -1.5
    linear = w1*x1 + w2*x2 + b
    return 1 if linear >= 0 else 0
def orGate(x1, x2):
    w1, w2, b = 1, 1, -0.5
    linear = w1*x1 + w2*x2 + b
    return 1 if linear >= 0 else 0
def nandGate(x1, x2):
    w1, w2, b = -2, -2, 3
    linear = w1*x1 + w2*x2 + b
    return 1 if linear >= 0 else 0
def norGate(x1, x2):
    w1, w2, b = -1, -1, 0.5
    linear = w1*x1 + w2*x2 + b
    return 1 if linear >= 0 else 0

def and_gate(x1, x2):
    y = 1 if x2 > -x1 + 1.5 else 0
    return y
def or_gate(x1, x2):
    y = 1 if x2 > -x1 + 0.5 else 0
    return y
def nand_gate(x1, x2):
    y = 1 if x2 <= -x1 + 1.5 else 0
    return y
def nor_gate(x1, x2):
    y = 1 if x2 <= -x1 + 0.5 else 0
    return y

def xor_gate(x1, x2):
    p = nand_gate(x1, x2)
    q = or_gate(x1, x2)
    return and_gate(p, q)