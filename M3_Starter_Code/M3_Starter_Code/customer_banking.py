# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("what is the balance of the savings account? : "))
    savings_interest = float(input("What is the apr for the savings account? : "))
    savings_maturity = int(input("how mant months will the savings account mature for? : "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("your earned interest : " + str(interest_earned))
    print("your updated savings account balance with interest earned : " + str(updated_savings_balance))
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("What is the starting balance of the cd account? : "))
    cd_interest = float(input("What is the apr for the cd account? : "))
    cd_maturity = int(input("How many months will the cd account mature for? : "))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_account, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your earned interest : " + str(interest_earned))
    print("Your updated cd account balance with interest earned : " + str(updated_cd_account))
if __name__ == "__main__":
    main()
    # Call the main function.
