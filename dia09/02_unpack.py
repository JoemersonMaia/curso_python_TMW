# %%

A=1
B=5

print(A)
print(B)

# %%
C=A
A=B
B=C
print(A)
print(B)

# %%

A, B= B, A

# %%
A, B, *_ = 1, 2, 3,31,3213,123,1231,3123,1
print(A, B, _)

# %%_
A, *resto, B = 1, 2, 3,31,3213,123,1231,3123,1
print(A, B, _)

# %%

def soma (a, *args):
    total = a+ sum(args)
    return total

soma( 1, 2 ,4 ,7)

# %%

def soma_quatro(a,b, c, d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)