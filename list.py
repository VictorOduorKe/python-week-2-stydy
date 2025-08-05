def check_if_number(input_list):
    numbers = []
    for x in input_list:
        try:
            num = float(x)
            numbers.append(num)
        except ValueError:
            print(f"Kindly enter numbers only. '{x}' is not a valid number.")
            return  # Stop further processing if a non-number is found
    print(f"The sum of {numbers} is {sum(numbers)}")

# Main program
numbers = input("Enter list of numbers separated by space: ")
input_list = numbers.split()
check_if_number(input_list)
