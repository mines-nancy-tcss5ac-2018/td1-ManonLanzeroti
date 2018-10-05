def solve(n):
    
    S=0
    N=str(n)
    for i in N:
        S += int(i)
        
    return S

assert solve(2**15)==26
print(solve(2**1000))