def INPUT(m):
    print(f"INPUT {m}")
def NOT(m, o):
    print(f"NOT {m} {o}")
def BNOT(m, o):
    print(f"BNOT {m} {o}")
def AND(m, n, o):
    print(f"AND 2 {m} {n} {o}")
def OR(m, n, o):
    print(f"OR 2 {m} {n} {o}")
def XOR(m, n, o):
    print(f"XOR 2 {m} {n} {o}")
def LSHIFT(m, n, o):
    print(f"LSHIFT {m} {n} {o}")
def RSHIFT(m, n, o):
    print(f"RSHIFT {m} {n} {o}")
def ZERO(m):
    AND(m, 100, m)
def MOV(m, o):
	BNOT(m, 99)
	BNOT(99, o)
def ADD(m, n, o):
	MOV(m, 71)
	MOV(n, 72)
	for i in range(16):
		XOR(71, 72, 74 + i)
		AND(71, 72, 73)
		LSHIFT(73, 1, 73)
		MOV(74 + i, 71)
		MOV(73, 72)
	MOV(89, o)
def SUB(m, n, o):
	MOV(n, 90)
	BNOT(90, 90)
	ADD(90, 1, 90)
	ADD(m, 90, o)
def CHECK():
	RSHIFT(18, 15, 18)
	AND(18, 1, 18)
	OR(17, 18, 17)
h, w = map(int, input().split())
INPUT(99)
INPUT(99)
for i in range(1, h * w + 1):
    INPUT(i + 20)
for i in range(1, 5):
    INPUT(i + 90)
NOT(1, 1)
for i in range(1, 16):
    ADD(i, 1, i + 1)
for i in range(h):
    for j in range(w):
        ZERO(17)
        ZERO(19)
        MOV(j, 18)
        SUB(18, 92, 18)
        CHECK()
        MOV(j, 18)
        SUB(94, 18, 18)
        CHECK()
        MOV(i, 18)
        SUB(18, 91, 18)
        CHECK()
        MOV(i, 18)
        SUB(93, 18, 18)
        CHECK()
        BNOT(19, 19)
        ADD(19, 17, 19)
        MOV(19, 41 + i * w + j)
for i in range(1, h * w + 1):	
    AND(i + 20, i + 40, i + 20)
    ADD(0, i + 20, 0)
for i in range(1, 100):
    ZERO(i)
