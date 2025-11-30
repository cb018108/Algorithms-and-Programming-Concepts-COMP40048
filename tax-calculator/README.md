Sri Lankan Personal Income Tax Calculator
Algorithm and Programming Concepts - COMP40048

### Introduction

This is a simple Python program to calculate Sri Lankan personal income tax based on monthly income. The program calculates annual and monthly tax and provides a breakdown.

As a first-year student, I learned to use basic Python like input, if-elif-else, and printing.

### 1) Task List

1. Read the monthly income from the user
2. Calculate annual income = monthly income x 12
3. Calculate annual taxable = annual income - 1800000
4. If taxable ≤ 0 → tax = 0
5. Calculate annual tax for slabs (6%, 18%, 24%, 30%, 36%)
6. Calculate monthly tax = annual tax / 12
7. Print the results (monthly income, annual income, annual tax, monthly tax)

### 2) Pseudocode

     START
          INPUT monthly_income     
          annual_income ← monthly_income × 12
          taxable ← annual_income − 1800000
     
               IF taxable ≤ 0 THEN
                    annual_tax ← 0
               ELSE
                    tax ← 0
                    remain ← taxable
          
                    // First 1,000,000 at 6%
                    IF remain > 1000000 THEN
                         tax ← tax + 1000000 × 0.06
                         remain ← remain − 1000000
                    ELSE
                         tax ← tax + remain × 0.06
                         remain ← 0
                    ENDIF
          
                    // Next 500,000 at 18%
                    IF remain > 500000 THEN
                         tax ← tax + 500000 × 0.18
                         remain ← remain − 500000
                    ELSE
                         IF remain > 0 THEN
                              tax ← tax + remain × 0.18
                              remain ← 0
                         ENDIF
                    ENDIF
          
                    // Next 500,000 at 24%
                    IF remain > 500000 THEN
                         tax ← tax + 500000 × 0.24
                         remain ← remain − 500000
                    ELSE
                         IF remain > 0 THEN
                              tax ← tax + remain × 0.24
                              remain ← 0
                         ENDIF
                    ENDIF
          
                    // Next 500,000 at 30%
                    IF remain > 500000 THEN
                         tax ← tax + 500000 × 0.30
                         remain ← remain − 500000
                    ELSE
                         IF remain > 0 THEN
                              tax ← tax + remain × 0.30
                              remain ← 0
                         ENDIF
                    ENDIF
          
                    // Rest at 36%
                    IF remain > 0 THEN
                         tax ← tax + remain × 0.36
                    ENDIF
          
                    annual_tax ← tax
               ENDIF
     
          monthly_tax ← annual_tax ÷ 12
     
          OUTPUT monthly_income, annual_income, annual_tax, monthly_tax
     STOP

### 3) Flowchart

(START)
↓
/Input/Read Monthly Income as monthly_income/
↓
[Calculate annual_income = monthly_income * 12]
↓
[Calculate taxable = annual_income - 1800000]
↓
{taxable ≤ 0} → Yes → annual_tax = 0 → Go to Output
↓ No
↓
remain = taxable, tax = 0
↓
Apply 6% on first 1,000,000 → reduce remain
↓
Apply 18% on next 500,000 → reduce remain
↓
Apply 24% on next 500,000 → reduce remain
↓
Apply 30% on next 500,000 → reduce remain
↓
Apply 36% on whatever is left
↓
annual_tax = total tax
↓
monthly_tax = annual_tax / 12
↓
Print all results → STOP

### 4) Example Test Case

**Input:**  
Enter your monthly income (LKR): 268000

**Expected Output:**  
Monthly Income : Rs. 268,000.00  
Monthly Tax : Rs. 11,240.00  
Annual Income : Rs. 3,21,6000.00  
Annual Tax : Rs. 134,880.00

**Verification:**  
268,000 × 12 = 3,216,000  
Taxable = 3,216,000 − 1,800,000 = 1,416,000  
First 1,000,000 × 6% = 60,000  
Next 416,000 × 18% = 74,880  
Total annual tax = 134,880 → Correct!
