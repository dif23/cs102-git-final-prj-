from data import *
from linkedlist import LinkedList
from time import sleep

print("\nHello! Welcome to Michael's Restaurant Recommender!!\n"); sleep(0.2)

#This function creates a linked list of the food types from data.py.
def insert_food_types():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert_beginning(food_type)
    return food_type_list

#This function creates a linked list of restaurants within the linked list of food types from data.py. Loops through the restaurants and adds restaurants to a list within each food type if there is a match.
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for food_type in types:
        restaurant_sublist = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == food_type:
                restaurant_sublist.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list

def one_food_choice():
    select_type = str(input("\nThe only matching type for the specified input is " + matching_types[0] + ". \n\nDo you want to look at " +
        matching_types[0] + " restaurants? Enter y for yes and n for no\n")).lower(); sleep(0.2)
        # Retrieves restaurant data here
    if select_type == 'y':
        selected_food_type = matching_types[0]
        print("\n\nSelected Food Type: " + selected_food_type); sleep(0.2)
        restaurant_list_head = my_restaurant_list.get_head_node()
        while restaurant_list_head.get_next_node() is not None:
            sublist_head = restaurant_list_head.get_value().get_head_node()
            if sublist_head.get_value()[0] == selected_food_type:
                while sublist_head.get_next_node() is not None:
                    print("\n\n--------------------------")
                    print("Name: " + sublist_head.get_value()[1])
                    print("Price: " + sublist_head.get_value()[2] + "/5")
                    print("Rating: " + sublist_head.get_value()[3] + "/5")
                    print("--------------------------\n\n")
                    sublist_head = sublist_head.get_next_node()
            restaurant_list_head = restaurant_list_head.get_next_node()
            # Narrows down the selection and gives the address
        choice_abv = str(input("\nWhat are the first three letters of the restaurant you want to try?\n")); sleep(0.2)
        restaurant_names = []
        for restaurant in restaurant_data:
            restaurant_names.append(restaurant[1])
        restaurant_abv = []
        for name in restaurant_names:
            restaurant_abv.append(name[:3])
        for abv in restaurant_abv:
            if abv == choice_abv:
                abv_index = restaurant_abv.index(abv)
                restaurant_choice = restaurant_names[abv_index]
                restaurant_address = restaurant_data[abv_index][4]
                print("\n\n--------------------------")
                print("Here's how to get there:")
                print(restaurant_choice)
                print(restaurant_address)
                print("--------------------------\n\n")

def multiple_food_choices():        
    matching_types_abv = []

    for food in matching_types:
        matching_types_abv.append(food[:3])

    print("\n\nThere's " + str(len(matching_types_abv)) + " possible types.\n\n"); sleep(0.2)
    
    select_type_abv = str(input("Type the first 3 letters of the food you want to try.\n\n")); sleep(0.2)

    for abv in matching_types_abv:
        if abv == select_type_abv:
            matching_type_abv_index = matching_types_abv.index(abv)
    
            food_type_choice = matching_types[matching_type_abv_index]

    select_type = str(input("\n\nDo you want to look at " +
        food_type_choice + " restaurants? Enter y for yes and n for no\n")).lower(); sleep(0.2)
        
       # Retrieves restaurant data here
    if select_type == 'y':
        selected_food_type = matching_types[matching_type_abv_index]
        print("\n\nSelected Food Type: " + selected_food_type); sleep(0.2)
        restaurant_list_head = my_restaurant_list.get_head_node()
        while restaurant_list_head.get_next_node() is not None:
            sublist_head = restaurant_list_head.get_value().get_head_node()
            if sublist_head.get_value()[0] == selected_food_type:
                while sublist_head.get_next_node() is not None:
                    print("\n\n--------------------------")
                    print("Name: " + sublist_head.get_value()[1])
                    print("Price: " + sublist_head.get_value()[2] + "/5")
                    print("Rating: " + sublist_head.get_value()[3] + "/5")
                    print("--------------------------\n\n")
                    sublist_head = sublist_head.get_next_node()
            restaurant_list_head = restaurant_list_head.get_next_node()


            # Narrows down the selection and gives the address

        choice_abv = str(input("\nWhat are the first three letters of the restaurant you want to try?\n")); sleep(0.2)

        restaurant_names = []

        for restaurant in restaurant_data:
            restaurant_names.append(restaurant[1])

        restaurant_abv = []

        for name in restaurant_names:
            restaurant_abv.append(name[:3])

        for abv in restaurant_abv:
            if abv == choice_abv:
                abv_index = restaurant_abv.index(abv)
                        
                restaurant_choice = restaurant_names[abv_index]
                restaurant_address = restaurant_data[abv_index][4]

                print("\n\n--------------------------")
                print("Here's how to get there:")
                print(restaurant_choice)
                print(restaurant_address)
                print("--------------------------\n\n")

#User input is taken here...
initial_food_list = []

for type in types:
    initial_food_list.append(type)
    
my_food_list = insert_food_types()
my_restaurant_list = insert_restaurant_data()

selected_food_type = ""

while len(selected_food_type) == 0:
    print("Here's a list of types of food you can find in the neighborhood...\n"); sleep(0.2)
    for i in types:
        print(types.index(i) +1, end=' ')
        print(" ",i); sleep(0.2)

    user_input = str(input("\nWhat kind of food are you looking for?\n\nType the first letter of the type of food and press return to see if you can find it in the neighborhood.\n\n")).lower()
    print("\n"); sleep(0.2)
    # Search for user_input in food types data structure here
    matching_types = []
    type_list_head = my_food_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    # print list of matching food types
    for i in matching_types:
        print(matching_types.index(i) +1, end=' ')
        print(" ",i); sleep(0.2)

    # Checks if only one type of restaurant was found, ask user if they would like to select this type
    if len(matching_types) == 1:
        one_food_choice()

    # Checks if more than one type of restaurant was found, asks user to narrow down selection
    elif len(matching_types) >= 1:
        multiple_food_choices()
        
    else:
        pass

# Ask user if they would like to search for other types of restaurants
    repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
    if repeat_loop == 'y':
        selected_food_type = ""
    elif repeat_loop == 'n':
        print("\nThank you and enjoy exploring new types of food!!\n\n")
        break
