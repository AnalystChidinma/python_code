"""
Bank Account Opening Validation System

Business Context:
This program simulates a basic customer validation system used by a bank 
to assess whether a new customer qualifies to open an account.

Objective:
To validate customer eligibility based on predefined business rules 
before approving account creation.

Inputs:
- Full Name (string)
- Age (integer)
- Initial Deposit Amount (float)
- Account Type (string: Savings or Current)

Business Rules:
1. Customer must be at least 18 years old.
2. Minimum deposit requirements:
   - Savings Account → 10,000
   - Current Account → 50,000
3. A 5% processing fee is deducted from the initial deposit.
4. Account type input should be case-insensitive.
5. Full name must be properly formatted (capitalized).

Outputs:
- Customer Name (formatted)
- Age
- Account Type
- Initial Deposit
- Processing Fee (if approved)
- Final Balance (if approved)
- Account Status (Approved or Rejected)
- Rejection Reason (if applicable)

Assumptions:
- User inputs valid numeric values for age and deposit.
- Currency is assumed to be in local denomination.

"""


# bank account validation system
customer_full_name = input("enter customer full name: ").strip().title()
customer_age = int(input("enter customer age: "))
customer_initial_deposit = float(input("enter initial deposit of customer: "))
account_type = input("enter the type of account (current/saving): ").strip().lower()

# age validation rules
if customer_age < 18:
      print(f"Account Rejected for {customer_full_name}.\n Rejection Reason: Customer must be at least 18 years old.")
      
# account validation rules
else:
      if account_type == "savings" and customer_initial_deposit < 10000:
            print(f"Account Rejected for {customer_full_name}. \n Rejection Reason: Minimum deposit for Savings Account is 10,000.")
      
      elif account_type == "current" and customer_initial_deposit < 50000:
                  print(f"Account Rejected for {customer_full_name}. \n Rejection Reason: Minimum deposit for Current Account is 50,000.")
      else:
            processing_fee = customer_initial_deposit * 0.05
            final_balance = customer_initial_deposit - processing_fee
            print(f"Account Approved for:{customer_full_name}.")
            print(f"Age: {customer_age}")
            print(f"Account Type: {account_type.title()}")
            print(f"Initial Deposit: {customer_initial_deposit}")
            print(f"Processing Fee: {processing_fee}")
            print(f"Final Balance: {final_balance}")
