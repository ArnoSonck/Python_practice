def run():
    my_list = [1, "Helo", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Soila", "lastname": "Mora"},
        {"firstname": "Susana", "lastname": "Oria"},
        {"firstname": "José", "lastname": "García"}
    ]

    super_dict = {
        "natural_numbers":[1, 2, 3, 4, 5],
        "integer_numbers":[-2, -1, 0, 1, 2],
        "floating_numbers":[-1.3, 1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    print("\n")

    for i in super_list:
        print(i["firstname"] , "-" , i["lastname"])

if __name__ == '__main__':
    run()