user_sales = int(input("Enter your sales: "))
while user_sales > 0:
    if user_sales <= 1000:
        bonus = user_sales * 0.1
        total_earning = user_sales + bonus
        print("Your bonus is ",bonus)
        print("Your total earning is ", total_earning)
        user_sales = int(input("Enter your sales: "))
    else:
        bonus = user_sales * 0.15
        total_earning = user_sales + bonus
        print("Your bonus is ", bonus)
        print("Your total earning is ", total_earning)
        user_sales = int(input("Enter your sales: "))
else:
    print("incorrect input")
    user_sales = int(input("Enter your sales: "))