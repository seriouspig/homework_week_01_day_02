# def greet(name, time_of_day):
#     #print("Hey")
#     return "Good " + time_of_day + ", " + name

# name_1 = "Bob"
# time_of_day_1 = "morning"
# greeting = greet(name_1,time_of_day_1)
# print(greeting)

# name_2 = "Ada"
# time_of_day_2 = "afternoon"
# greeting = greet(name_2, time_of_day_2)
# print(greeting)

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

chickens_2 = [
  { "name": "Margaret", "age": 2, "eggs": 15 },
  { "name": "Hetty", "age": 1, "eggs": 23 },
  { "name": "Henrietta", "age": 3, "eggs": 32 },
  { "name": "Audrey", "age": 2, "eggs": 43 },
  { "name": "Mabel", "age": 5, "eggs": 23 },
]

def count_eggs( list ):
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return f"{total_eggs} eggs collected"

print(count_eggs(chickens))

print(count_eggs(chickens_2))

# def greet():
#     words = "Hey"
#     return words

# def greet_two():
#     return words

# print(greet_two())


# def wash_clothes(laundry, detergent):
#     clean_laundry = laundry + detergent + water
#     return clean_laundry

# clean_tshirt = wash_clothes("dirty_tshirt", "liquid_detergent")