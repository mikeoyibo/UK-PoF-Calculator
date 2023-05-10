print("Simple program to calculate Proof of Funds")

tuition = int(input("\nEnter total tuition fee: "))

deposit = int(input("Enter deposit paid: "))

dependants = int(input("How many dependants are do you have: "))

location = input("Is your univesity in London? If Yes, Type 'y', if No, Enter 'n': ")


if location == "y":
    fee_balance = tuition - deposit
    x = fee_balance + 12006
    y = 7605 * dependants  # for London as at 2023 7605
    z = x + y
    k = z * 579.983

    print(f"Your PoF is estimated to be £{z:,} or ₦{k:,}")

else:
    fee_balance = tuition - deposit
    x = fee_balance + 9207
    y = 6120 * dependants
    z = x + y
    k = z * 579.983
    print(
        f"Since you are schooling outside London, your PoF is estimated to be £{z:,} or ₦{k:,}"
    )
