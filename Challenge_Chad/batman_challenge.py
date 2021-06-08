hero = {
    'name':
        {
            'alias':'Batman',
            'real name':'Bruce Wayne'
        },
    'background':
        {
            'origin':'Parents got murdered, got angry. Is super rich.',
            'family':
                {
                    'parents':'dead',
                    'siblings':None
                },
            'age':32,
            'number of deaths':19
        },
    'powers':
        ['ninja training','money','batsuit'],
    'enemies':['joker','two face','scarecrow','poison ivy'],
    'allies':['cat woman','red robin','nightwing'],
    'rivals':['joker'],
    'weaknesses':['poverty','strict moral code']
}

# Python functions
# @https://www.w3schools.com/python/python_functions.asp
def printName(hero_obj):
    print(f"alias name: {hero_obj.get('name').get('alias')}")
    print(f"real name: {hero_obj.get('name').get('real name')}")

def printBackground(hero_obj):
    print(f"Origin: {hero_obj.get('background').get('origin')}")
    print(f"Family: {hero_obj.get('background').get('family')}")
    print(f"Age: {hero_obj.get('background').get('age')}")
#    print(hero_obj["background"])

def printAllPowers(hero_obj):
    print(f"Power(s): {hero_obj.get('powers')}")

def printAllEnemies(hero_obj):
    print(f"Enemies: {hero_obj.get('enemies')}")

def printAllAllies(hero_obj):
    print(f"Allies: {hero_obj.get('allies')}")

def printRival(hero_obj):
    print(f"Rival: {hero_obj.get('rivals')}")

def printAllWeaknesses(hero_obj):
    print(f"Weaknesses: {hero_obj.get('weaknesses')}")

default_behavior = True
# controller
while (default_behavior):
    print("Welcome to About Batman")
    selection = input("Select a category (\nName\nBackground\nPowers\nEnemies\nAllies\nRivals\nWeaknesses)\n> ").lower()
    hero_selected_category = hero.get(selection)
    if hero_selected_category and selection == 'name':
        printName(hero)
    elif hero_selected_category and selection == 'background':
        printBackground(hero)
    elif hero_selected_category and selection == 'powers':
        printAllPowers(hero)
    elif hero_selected_category and selection == 'enemies':
        printAllEnemies(hero)
    elif hero_selected_category and selection == 'allies':
        printAllAllies(hero)
    elif hero_selected_category and selection == 'rivals':
        printRival(hero)
    elif hero_selected_category and selection == 'weaknesses':
        printAllWeaknesses(hero)
    else:
        print("Not a good selection")
    user_choice = input("Do you want to try it again? (y/n)")
    if user_choice == 'n':
        default_behavior = False
    else:
        print("=============================")
        print("=============================")
