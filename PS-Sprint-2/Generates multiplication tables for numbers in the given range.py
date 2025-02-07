def generate_multiplication_table(start, end, upto=10):
    """Generates multiplication tables for numbers in the given range."""
    for num in range(start, end + 1):
        print(f"\nMultiplication Table for {num}:\n" + "-" * 25)
        for i in range(1, upto + 1):
            print(f"{num} x {i} = {num * i}")
        print("-" * 25)

# Example Usage:
start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))
upto = int(input("Enter the range (default is 10): "))

generate_multiplication_table(start_num, end_num, upto)
