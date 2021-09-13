# r = 0.2

# 1000$
# 1200$ = 1000 + (0.2 * 1000) = 1.2 * 1000 = 1200
# 1440$ = 1200 * (1 + r) = 1440

def calc_bank_investment(initial_mony, num_of_years, rate = 0.2):
    result = initial_mony

    for i in range(num_of_years):
        # a = a * 1
        # a *= 1
        result *= (1 + rate)
     

    return result


print(calc_bank_investment(num_of_years=3, initial_mony=1000))