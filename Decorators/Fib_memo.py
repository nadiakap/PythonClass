#import time
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:    
            memo[x] = f(x)
        #print(memo)
        return memo[x]
    
    return helper
 

def iter_fib(n):
    prev = 1
    prev_prev = 0
    print(prev_prev)
    print(prev)
    for i in range(n):
        new = prev + prev_prev
        prev_prev = prev
        prev = new
        print(new)
        

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib = memoize(fib)
'''
t1=time.time()
print(fib(10))
t2=time.time()
print(('fib takes  %0.12f') % (t2-t1))


'''
res = fib(20)
fib = memoize(fib)
res = fib(10)
print(res)
