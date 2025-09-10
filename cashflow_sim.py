import numpy as np

discount_rate = 0.08
cashflows = [-100] + [30, 35, 40, 45, 50]  # capex + 5 years of returns

npv = sum(cf / (1+discount_rate)**t for t, cf in enumerate(cashflows))
print("NPV:", npv)
