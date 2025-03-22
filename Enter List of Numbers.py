# Write a function that takes a list of numbers as input 
# and returns the sum of all the even numbers in the list.

number_list = []
even_number_list = [] 
total_sum = 0

def find_even_numbers():
    for number in number_list:
        if number % 2 == 1:
            return "odd"
        else:
            even_number_list.append(number)
    return None

def sum_of_even_numbers(): 
    global total_sum
    for number in even_number_list:
        total_sum += number

def main():
    global total_sum

    while True:
        number_list_input = input("Enter a list of numbers (or quit): ")
        if number_list_input == "quit":
            print("Exiting...")
            break
        else:
            number_list.append(int(number_list_input))

    if find_even_numbers() != "odd":
        sum_of_even_numbers()
        print(f"Total Sum of Even Numbers: {total_sum}")
    else:
        print("List contains an odd number, cannot sum even numbers.")

main()