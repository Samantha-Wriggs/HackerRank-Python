import cmath

val = raw_input()
r = abs(complex(val))
p = cmath.phase(complex(val))

print(r)
print(p)
