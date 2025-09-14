import numpy as np

n_years = 5
n_sims = 1000
discount_rate = 0.08

capex_mean = 100
capex_std = 5
revenue_means = [30, 35, 40, 45, 50]
revenue_std = 5

npvs = []

for sim in range(n_sims):
    capex = -np.random.normal(capex_mean, capex_std) # generates a single value
    revenues = np.random.normal(revenue_means, revenue_std)  # generates an array of 5 values for 5 years depending on means and std
    cashflows = [capex] + revenues.tolist() # cashflow is a list with capex followed by revenues
    npv = sum(cf / (1+discount_rate)**t for t, cf in enumerate(cashflows)) #NPV is calculated as the sum of cashflows discounted to present value
    npvs.append(npv)

print("Mean NPV:", np.mean(npvs)) # Mean NPV across all simulations
print("Probability NPV > 0:", np.mean(np.array(npvs) > 0)) # Probability that NPV is greater than 0
