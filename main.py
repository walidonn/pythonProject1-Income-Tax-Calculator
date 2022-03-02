def taxIncome(gross, dependents):
    ans = 0
    if dependents > 0:
        deduction = gross - (10000 + 3000 * dependents)
        ans = (20 / 100) * deduction

    return ans


print(taxIncome(150000.00, 3))
