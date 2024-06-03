import csv
from enum import Enum


diamonds = []


class Actions(Enum):
    HIGHEST_DIAMOND_PRICE = 1
    AVERAGE_DIAMOND_PRICE = 2
    HOW_MANY_IDEAL_DIAMONDS_EXISTS = 3
    HOW_MANY_DIAMOND_COLORS = 4
    MID = 5
    CUT_CARAT_AVERAGE = 6
    AVERAGE_COLOR_PRICE = 7
    EXIT = 8


def load_diamonds(filename):
    diamonds = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            diamonds.append(row)
    return diamonds


def display_menu():
    for action in Actions:
        print(f'{action.name}-{action.value}')
    return Actions(int(input("Your choice?")))


def highest_diamond_price(diamonds):
    return max(diamonds, key=lambda diamond: float(diamond['price']))
   

def average_price(diamonds):
    total_price = sum(float(diamond['price']) for diamond in diamonds)
    return total_price / len(diamonds)


def how_many_ideal_diamonds(diamonds):
    ideal_count = sum(1 for diamond in diamonds if diamond['cut'] == 'Ideal')
    return ideal_count
    

def how_many_diamond_colors(filename):
    diamond_colors = set() 
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            diamond_colors.add(row['color'])  
    return len(diamond_colors), list(diamond_colors)


def mid_carat_premium(filename):
    with open(filename, newline='') as csvfile:
        carats = [float(row['carat']) for row in csv.DictReader(csvfile) if row['cut'] == 'Premium']
    carats.sort()
    n = len(carats)
    mid = (carats[n // 2 - 1] + carats[n // 2]) / 2 if n % 2 == 0 else carats[n // 2]
    print(f"The mid carat for Premium diamonds is {mid}")
    return mid


def average_carat_cut(diamonds):
    carat_sum_per_cut = {}
    count_per_cut = {}
    for diamond in diamonds:
        cut = diamond['cut']
        carat = float(diamond['carat'])
        carat_sum_per_cut[cut] = carat_sum_per_cut.get(cut, 0) + carat
        count_per_cut[cut] = count_per_cut.get(cut, 0) + 1
    for cut, carat_sum in carat_sum_per_cut.items():
        count = count_per_cut[cut]
        average_carat_per_cut = carat_sum / count
        print(f"The average carat for {cut} diamonds is {average_carat_per_cut}")


def average_price_color(diamonds):
    price_sum_color = {}
    count_per_color = {}
    for diamond in diamonds:
        color = diamond['color']
        price = float(diamond['price'])
        price_sum_color[color] = price_sum_color.get(color, 0) + price
        count_per_color[color] = count_per_color.get(color, 0) + 1
    for color, price_sum in price_sum_color.items():
        print(f"The average price for {color} diamonds is: {price_sum / count_per_color[color]}")
    return {color: price_sum / count_per_color[color] for color, price_sum in price_sum_color.items()}




if __name__== "__main__":
 diamonds = load_diamonds('data.csv')
 while True:
    user_selection= display_menu()
    if user_selection == Actions.EXIT : exit()
    if user_selection == Actions.HIGHEST_DIAMOND_PRICE:
            highest_price_diamond = highest_diamond_price(diamonds)
            print(f"The highest diamond price is: {highest_price_diamond['price']}")
    if user_selection == Actions.AVERAGE_DIAMOND_PRICE: 
            average_price = average_price(diamonds)
            print(f"The average diamond price is: {average_price}")
    if user_selection == Actions.HOW_MANY_IDEAL_DIAMONDS_EXISTS: 
            ideal_count = how_many_ideal_diamonds(diamonds)
            print(f"There are {ideal_count} Ideal diamonds")
    if user_selection == Actions.HOW_MANY_DIAMOND_COLORS: 
            colors_count = how_many_diamond_colors('data.csv')
            print(f"There are {colors_count} diamond colors")
    if user_selection == Actions.MID: mid_carat_premium('data.csv')
    if user_selection == Actions.CUT_CARAT_AVERAGE: average_carat_cut(diamonds)
    if user_selection == Actions.AVERAGE_COLOR_PRICE: average_price_color(diamonds)
    
