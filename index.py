def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if final_price == price:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
