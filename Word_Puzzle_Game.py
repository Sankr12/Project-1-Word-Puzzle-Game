import random

my_list = ["pyla" , "rac" , "owlf" , "lkaw" , "cehck" , "elpap" , "rdib" , "itnac" , "nacemhi" , "rafct" , "etbla" , "tilgh" , "ikle"]
answers = ["play" , "car" , "wolf" , "walk" , "check" , "apple" , "bird" , "antic" , "machine" , "craft" , "table" , "light" , "like"]

num_random = 5

random_items = random.sample(my_list, num_random)

result = 0
print()

for item in random_items:
    print(item, "\n")
    answer = input("Enter the correct word for {}: ".format(item))
    i = my_list.index(item)

    if answer == answers[i]:
        print("\nRight Answer!\n")
        result += 1
    else:
        print("\nWrong Answer!\n")
        result -= 1

print("Your Score:", result)
print()
