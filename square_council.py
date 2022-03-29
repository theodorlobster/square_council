import random

if __name__ == "__main__":
    # Load nouns list
    with open('./n.txt', 'r') as fd:
        noun_list = [f.strip() for f in fd.readlines()]
    # Load adjectives list
    with open('./a.txt', 'r') as fd:
        adj_list = [f.strip() for f in fd.readlines()]
    # Loop 'til you get bored
    i = 'y'
    while i.lower() == 'y':
        name = random.choice(adj_list).capitalize() + ' ' + random.choice(noun_list).capitalize()
        print(name)
        i = input("One more try ? y/n : ")
    if i.lower() != 'n':
        print("Command not in options. Exit")