def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    text = input()
    parts = text.split(",")
    numbers = []
    for p in parts:
        numbers.append(float(p))
    return numbers

def calc_average(num_list):
    return sum(num_list) / len(num_list)

def find_min_max(num_list):
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    return sorted(num_list)
# Returns the median of the list (sorted first)
def calc_median_temperature(num_list):
    s = sorted(num_list)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("Average = " + str(calc_average(num_list)))
    print("Min and Max = " + str(find_min_max(num_list)))
    print("Sorted = " + str(sort_temperature(num_list)))
    print("Median = " + str(calc_median_temperature(num_list)))

if __name__ == "__main__":
    main()