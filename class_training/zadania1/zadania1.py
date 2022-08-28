import random

def return_string(*args):
    combined_string = ""
    for str in args:
        if len(combined_string) == 0:
            combined_string = str
        else:
            combined_string += "-" + str
    return combined_string

def print_values(**kwargs):
    for key, value in kwargs.items():
        print(key + "=" + str(value))

def generate_list(volume):
    list_of_numbers = []
    for _ in range(volume):
        number = random.randint(1, 100)
        list_of_numbers.append(number)
    return list_of_numbers

def run_example():
    #print(return_string("Ala", "ma", "kota"))
    # print_values(
    #     first_name = "Mikolaj",
    #     age="134"
    # )
    # first_list = generate_list(10)
    # second_list = generate_list(5)
    # final_list = [*first_list, *second_list]
    # print(first_list)
    # print(second_list)
    # print(final_list)
    first_dictionary = {
        "first_name": "Pawel",
        "last_name": "Latocha",
        "age": 32
    }
    second_dictionary = {
        "city": "Krakow",
        "zip-code": "30-502"
    }
    final_dictionary = {**first_dictionary, **second_dictionary}
    print_values(**final_dictionary)



if __name__ == "__main__":
    run_example()

