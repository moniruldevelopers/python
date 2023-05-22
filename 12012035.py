def find_longest_string(list):
    longest_string = ""
    for string in list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


if __name__ == "__main__":
    list = list(map(str, input("Enter a list of strings: ").split()))
    print("The longest string in the list is:", find_longest_string(list))
