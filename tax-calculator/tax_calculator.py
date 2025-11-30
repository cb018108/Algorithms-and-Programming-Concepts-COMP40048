# Sri Lankan Personal Income Tax Calculator

# Ask: Monthly Income
monthly_income = float(input("Enter your monthly income (LKR): "))

# Calculate annual income and taxable amount
annual_income = monthly_income * 12
taxable = annual_income - 1800000

# Calculate tax
if taxable <= 0:
    annual_tax = 0
else:
    tax = 0
    remain = taxable

    # First 1,000,000 at 6%
    if remain > 1000000:
        tax = tax + 1000000 * 0.06
        remain = remain - 1000000
    else:
        tax = tax + remain * 0.06
        remain = 0

    # Next 500,000 at 18%
    if remain > 500000:
        tax = tax + 500000 * 0.18
        remain = remain - 500000
    else:
        if remain > 0:
            tax = tax + remain * 0.18
            remain = 0

    # Next 500,000 at 24%
    if remain > 500000:
        tax = tax + 500000 * 0.24
        remain = remain - 500000
    else:
        if remain > 0:
            tax = tax + remain * 0.24
            remain = 0

    # Next 500,000 at 30%
    if remain > 500000:
        tax = tax + 500000 * 0.30
        remain = remain - 500000
    else:
        if remain > 0:
            tax = tax + remain * 0.30
            remain = 0

    # Rest at 36%
    if remain > 0:
        tax = tax + remain * 0.36

    annual_tax = tax

# Calculate monthly tax
monthly_tax = annual_tax / 12

# Print results
print("=====================================")
print("     SRI LANKAN TAX CALCULATOR       ")
print("=====================================")
print(f"Monthly Income     : Rs. {monthly_income:,.2f}")
print(f"Monthly Tax        : Rs. {monthly_tax:,.2f}")
print(f"\nAnnual Income      : Rs. {annual_income:,.2f}")
print(f"Annual Tax         : Rs. {annual_tax:,.2f}")
print("=====================================")
