def compute_pay(hours, salary, overpay):
    extra_h = max(0,hours - 40)
    reg_h = min(hours, 40)
    return extra_h * overpay + reg_h * salary

def compute_change(amount, cost):
    change = amount - cost
    d = {20: 0, 10: 0, 5: 0, 1: 0}
    
    for i in d.keys():
        d[i] = int(change / i)
        change = change % i
    
    return d


          

if __name__=='__main__':
    
    hours = 50
    salary = 60
    overpay = 75
    result = compute_pay(hours, salary, overpay)
    print('total pay:', result)

    result2 = compute_change(100, 57)
    print('change:', result2)
