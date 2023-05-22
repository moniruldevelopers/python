def sum_of_even_numbers(list):
    sum = 0
    for x in list:
        if x % 2 == 0:
            sum += x
    return sum

if __name__== "__main__":
    list = list(map(int,input("enter your list of integers", ).split()))

print("Your enter list of intergers even number sum is : ", sum_of_even_numbers(list))