def run():
    # Making dictionaries with for
    n = input("Chose a integer number: ")
    n = int(n)
    my_index ={}
    for i in range(1,n+1):
        my_index[i] = i**3
    print(my_index)

    # Only keeping non divisible by 3 numbers
    # I tried to use my_index in the for cicle
    # but was no posible because my_index change of size.
    for i in range(1,n+1):
        if my_index[i]%3==0:
            del my_index[i]
    print(my_index)

    # Using dictionary comprehesions
    my_dictionary = {i:i**3 for i in range(1,n+1) if i%3 != 0}
    print(my_dictionary)

    # Challenge: 
    my_square_dictionary={i:i**(1/2) for i in range(1,n+1)}
    print(my_square_dictionary)


if __name__ == '__main__':
    run()