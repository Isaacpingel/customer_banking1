# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account 
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_starting_balance = float(input("Enter your starting balance: "))
    interest_rate = float(input("Please enter your monthly interest rate: "))
    months = int(input("How many months have you had this account? "))

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_starting_balance, interest_rate, months)
    print(f"Here is your monthly interest: {interest_earned} ")
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Here is your monthly interest: {interest_earned} ")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_savings_balance = float(input("Enter your starting balance: "))
    cd_interest_rate = float(input("Please enter your monthly interest rate: "))
    months = float(input("How many months have you had this account? "))
    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    cd_savings_balance, cd_interest_earned = create_cd_account(savings_starting_balance, cd_interest_rate, months)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Here is your monthly interest: {cd_updated_balance} ")
if __name__ == "__main__":
    # Call the main function.
    main()