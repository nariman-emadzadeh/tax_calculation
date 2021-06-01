# Allows to keep the list in sorted order after insertion of each element

from bisect import bisect

# Different tax rates for each bracket
rates = [10, 12, 22, 24, 32, 35, 37]   # 10%  12%  22%


"""
"TABLE 2 - Section 1(j)(2)(B) – Heads of Households"

brackets = [14200,        # first 14,200
            54200,        # next  54,200
            86350,
            164900,
            209400,
            523600]        # next  523,600

base_tax = [1420,            # 10,000 * 0%
            4800,         # 20,000 * 10%
            7073,
            18852,
            67008,
            109970]        # 40,000 * 20% + 2,000
"""

"TABLE 3 - Section 1(j)(2)(C) – Unmarried Individuals (other than Surviving Spouses and Heads of Households)"
brackets = [9950,        # first 14,200
            40525,        # next  54,200
            86375,
            164925,
            209425,
            523600]        # next  523,600

base_tax = [995,            # 10% of $9950 (taxable income)
            4664,         # 12% over $9950 but not over $40,525 plus the $995 which was the 10% of the first bracket ($9950)
            14751,
            33603,
            47843,
            157804]        # 40,000 * 20% + 2,000






def tax(income):
    i = bisect(brackets, income)
    if not i:
        return 0
    rate = rates[i]
    bracket = brackets[i-1]
    income_in_bracket = income - bracket
    tax_in_bracket = income_in_bracket * rate / 100
    total_tax = base_tax[i-1] + tax_in_bracket
    return total_tax

# input your taxable income
taxable_income = input("what is your taxable income?")
user_income = float(taxable_income)

print("The total tax owed to IRS based on your net income of",user_income, "is:", tax(user_income))

