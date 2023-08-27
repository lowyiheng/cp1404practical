"""
Replace the contents of this module docstring with your own details
Name: Low Yi Heng
Date started: 19th AUGUST 2023
GitHub URL: https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-1-lowyiheng.git
"""

import csv
import random

MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by <Low Yi Heng>")
    city_list = read_file(FILENAME)
    city_list = sorted(city_list, key=by_priority, reverse=True)
    print(f"{(len(city_list))} places loaded from {FILENAME}")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            list_places(city_list)
        elif choice == "R":
            recommend_place(city_list)
        elif choice == "A":
            add_place(city_list)
        elif choice == "M":
            list_places(city_list)
            mark_visited(city_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_file(FILENAME, city_list)
    print(f"{(len(city_list))} places saved to {FILENAME}\nHave a nice day :)")


def read_file(filename):
    city_list = []
    with open(filename, "r") as in_file:
        for line in in_file:
            city_info = line.strip().split(",")
            city_list.append(city_info)
        in_file.close()
    return city_list


def save_file(filename, city_list):
    with open(filename, "w", newline='') as out_file:
        city_writer = csv.writer(out_file)
        for place_info in city_list:
            city_writer.writerow(place_info)
        out_file.close()


def by_priority(priority):
    return priority[2]


def list_places(city_list):
    unvisited_number = 0
    for i, city in enumerate(city_list):
        if city[-1] == "n":
            visited = "*"
            unvisited_number += 1
        else:
            visited = " "
        print(f"{visited}{i + 1}.{city[0]:<15} in {city[1]:<15}{city[2]:>5}")
    if unvisited_number == "0":
        print(f"{len(city_list)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(city_list)} places. You still want to visit {unvisited_number} places.")


def recommend_place(city_list):
    unvisited_places = []
    for city in city_list:
        if city[-1] == "n":
            unvisited_places.append(city[0])
    if not unvisited_places:
        print("No unvisited places")
    else:
        name = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {name} in {city[1]}?")


def add_place(city_list):
    place_name = check_blank("Name: ")
    place_country = check_blank("Country: ")
    place_priority = input("Priority: ")
    while not place_priority.isdigit():
        print("Priority must be a number")
        place_priority = input("Priority: ")
    place_info = [place_name, place_country, place_priority, "n"]
    city_list.append(place_info)
    print(f"{place_name} in {place_country} (priority {place_priority}) added to Travel Tracker")


def check_blank(prompt):
    info = input(prompt)
    while info == "":
        print("Input can not be blank")
        info = input(prompt)
    return info


def mark_visited(city_list):
    if is_visited(city_list):
        is_valid = True
        print("Enter the number of a place to mark as visited")
        while is_valid:
            index_input = input(">>> ")
            if index_input.isdigit():
                is_valid = False
                index = int(index_input)
                if index not in range(1, len(city_list) + 1):
                    if index >= len(city_list) + 1:
                        print("Invalid place number")
                    else:
                        print("Number must be > 0")
                    is_valid = True
                else:
                    if city_list[index - 1][-1] == "n":
                        print(f"{city_list[index - 1][0]} in {city_list[index - 1][1]} visited!")
                        city_list[index - 1][-1] = "v"
                    else:
                        print(f"You have already visited {city_list[index - 1][0]}")
            else:
                is_valid = True
                print("Invalid input; enter a valid number")
    else:
        print("No unvisited places")


def is_visited(city_list):
    for city in city_list:
        if city[3] == "n":
            return True
    return False


if __name__ == '__main__':
    main()