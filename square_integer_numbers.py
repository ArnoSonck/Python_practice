def run():
    n = input("Up to what number do you want to know its squares: ")
    print("You chosed: " + n)
    my_list = []
    for i in range(1,int(n)+1):
        my_list.append(i*i)
    
    print("Theirs squares are: \n", my_list, "\n")

    # keeping only numbers divisible by 3
    only_three = []
    for i in range(0,int(n)):
        if my_list[i] % 3 == 0:
            only_three.append(my_list[i])
    
    print("Theirs members that are only divisible by 3 are: \n", only_three, "\n")

    # Avoiding divisors of 4, 6, and 9.
    # Notice that the least common multiple is 36
    # Using List Comprehisions
    no_36_list = [i**2 for i in range(1,int(n)+1) if i**2 % 36 == 0]
    print("Keeping only divisible by 4, 6, and 9 numbers: \n", no_36_list)

if __name__ == '__main__':
    run()