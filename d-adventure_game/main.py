# Adventure Game -
from utilities import clear , style , press_key , sleep

GAME_STATE = {
    "health": 10,
    "inventory": {
        "energy": 50,
        "silver": 0,
        "gold": 0,
        "key": 0
    }
}

def valid_input():
    '''
    takes the different inputs but find the closest and return : r for right and l for left
    '''   
    while True:
        user = input("\n    RIGHT or LEFT???\n    Enter your choice : ").lower()
    # check if empty
        if not user:
            style("\n    Empty input...\n    Try Again...\n",0.02)
            sleep(1)
            continue
    # check for inventory
        if user[0]=='x':
            if user == 'x' or user =='inventory':
                user = 'x'
                return user
            continue
    # check if its right
        if user[0]=='r':
            if user == 'r' or user =='rock':
                user = 'r'
                return user
            else:
                ask = input("    Did you mean RIGHT ? (y/n) : ")
                if ask == 'y':
                    user = 'r'
                    return user
                else:
                    style("\n    ummm, we could not guess your input.\n    Try Again...\n",0.02)
                    sleep(2)
    # check if its left
        elif user[0]=='l':
            if user == 'l' or user =='left':
                user = 'l'
                return user
            else:
                ask = input("    Did you mean LEFT ? (y/n) : ")
                if ask == 'y':
                    user = 'l'
                    return user
                else:
                    style("\n    ummm, we could not guess your input.\n    Try Again...\n",0.02)
                    sleep(2)
    # if could not understand
        else:
            style("\n    ummm, we could not guess your input.\n    Try Again...\n",0.02)
            sleep(2)

def data_logic(effect):
    '''
    data handling for the health and inventory in the game
    it can be : 
    : param l=[ "health" , "action" , amount  ]
    OR can be
    : param l=[ "inventory" , "action" ,  amount  , "type" ]
    
    l[0] : str : health or inventory
    l[1] : str : add or reduce
    l[2] : int : amount to be added or reduced
    l[3] : str : (only when l[0] is inventory) : type of utility
    '''

    if effect[0] == "health":
        action = effect[1]
        amount = effect[2]

        if action == "add" and GAME_STATE["health"]<=10:            
            GAME_STATE["health"] += amount
            if GAME_STATE["health"] > 10:
                GAME_STATE["health"] = GAME_STATE["health"] - (GAME_STATE["health"]-10)
        elif action == "reduce" and GAME_STATE["health"] >0 :
            GAME_STATE["health"] -= amount

    elif effect[0] == "inventory":
        action = effect[1]
        utility = effect[2]
        amount = effect[3]

        if action == "add":
            GAME_STATE["inventory"][utility] += amount
        else:
            GAME_STATE["inventory"][utility] = max(0, GAME_STATE["inventory"][utility] - amount)

def story(location):

    story_tree = {

        # ---------------------------------------------------
        # 1. START
        # ---------------------------------------------------
        "main": {
            "text":
                "You wake up inside ancient stone ruins.\n"
                "    Moss covers broken walls.\n"
                "    A cold wind whispers.\n"
                "\n"
                "    Two passages lie ahead...",
            "choices": {
                "l": "Hall of Echoes",
                "r": "Collapsed Chamber"
            },
            "effects": {
                "l": [["inventory", "reduce", "energy", 5]],
                "r": [["inventory", "reduce", "energy", 5]]
            }
        },

        # ---------------------------------------------------
        # 1B EXTRA BRANCH — Collapsed Chamber
        # ---------------------------------------------------
        "Collapsed Chamber": {
            "text":
                "You enter the collapsed hall.\n"
                "    Dust falls from the ceiling.\n"
                "    A narrow gap leads forward.\n"
                "\n"
                "    A faint light flickers deeper inside.",
            "choices": {
                "l": "Squeeze Through Gap",
                "r": "Climb Over Debris"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5],["health","reduce",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Squeeze Through Gap": {
            "text":
                "You squeeze through the gap.\n"
                "    Sharp stones scrape your skin.\n"
                "    A tunnel stretches ahead.",
            "choices": {
                "l": "Follow the Tunnel",
                "r": "Return to Ruins Entrance"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Climb Over Debris": {
            "text":
                "You climb over unstable rubble.\n"
                "    A hidden opening leads to the forest gate hall.",
            "choices": {
                "l": "Hall of Echoes",
                "r": "Dark Staircase"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Follow the Tunnel": {
            "text":
                "You follow the dark tunnel.\n"
                "    It opens up into a massive natural cavern.",
            "choices": {
                "l": "Cross the Cavern Bridge",
                "r": "Take the Lower Path"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Return to Ruins Entrance": {
            "text":
                "You retraced your steps...\n"
                "    But the entrance is blocked.\n"
                "    You must find another way.",
            "choices": {
                "l": "Hall of Echoes",
                "r": "Dark Staircase"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # 2. HALL OF ECHOES
        # ---------------------------------------------------
        "Hall of Echoes": {
            "text":
                "You step into a vast corridor.\n"
                "    Your footsteps echo endlessly.\n"
                "    A faint humming vibrates through the air.\n"
                "\n"
                "    Ahead lies a glowing doorway and a dark staircase.",
            "choices": {
                "l": "Glowing Doorway",
                "r": "Dark Staircase"
            },
            "effects": {
                "l": [["inventory","reduce","energy",5]],
                "r": [["inventory","reduce","energy",5],["health","reduce",5]]
            }
        },

        # ---------------------------------------------------
        # 3A. GLOWING DOORWAY
        # ---------------------------------------------------
        "Glowing Doorway": {
            "text":
                "A serene chamber greets you.\n"
                "    Hundreds of floating lights drift in silence.\n"
                "    A calm, gentle spirit materializes.\n"
                "\n"
                "    'Traveler… I offer you a blessing… for a price.'",
            "choices": {
                "l": "Accept Blessing",
                "r": "Refuse and Continue"
            },
            "effects": {
                "l": [
                    ["health","add",20],
                    ["inventory","reduce","energy",5],
                    ["inventory","reduce","silver",2]
                ],
                "r": [["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # 3B. DARK STAIRCASE
        # ---------------------------------------------------
        "Dark Staircase": {
            "text":
                "You descend into suffocating darkness.\n"
                "    Something skitters behind you.\n"
                "    A crawling creature leaps from the shadows!",
            "choices": {
                "l": "Fight the Creature",
                "r": "Run Back Upstairs"
            },
            "effects": {
                "l":[["health","reduce",15],["inventory","add","silver",5],["inventory","reduce","energy",5]],
                "r":[["health","reduce",10],["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # 4A. ACCEPT BLESSING
        # ---------------------------------------------------
        "Accept Blessing": {
            "text":
                "Warm light wraps around you.\n"
                "    Your wounds fade.\n"
                "    A hidden stone door creaks open,\n"
                "    revealing an ancient bridge ahead.",
            "choices": {
                "l": "Cross the Bridge",
                "r": "Explore Side Tunnel"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # 4B. REFUSE BLESSING
        # ---------------------------------------------------
        "Refuse and Continue": {
            "text":
                "You step past the spirit.\n"
                "    The chamber grows colder.\n"
                "    Faint whispers echo behind you.\n"
                "\n"
                "    Another chamber lies ahead.",
            "choices": {
                "l": "Enter Carved Chamber",
                "r": "Follow Narrow Crack"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # 5A. FIGHT CREATURE
        # ---------------------------------------------------
        "Fight the Creature": {
            "text":
                "Breathing hard, you stand over the fallen beast.\n"
                "    Behind it lies a tunnel carved with ancient symbols.",
            "choices": {
                "l": "Follow the Symbol Tunnel",
                "r": "Loot the Creature"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5],["inventory","add","gold",3]]
            }
        },

        # ---------------------------------------------------
        # 5B. RUN BACK UPSTAIRS
        # ---------------------------------------------------
        "Run Back Upstairs": {
            "text":
                "You burst back into the upper halls.\n"
                "    A small alcove carved with symbols invites you to rest.",
            "choices": {
                "l": "Rest Here",
                "r": "Push Forward Again"
            },
            "effects": {
                "l":[["health","add",10],["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # MID-GAME LOCATIONS
        # ---------------------------------------------------
        "Cross the Bridge": {
            "text":
                "The old bridge trembles as you cross.\n"
                "    In the center, a glowing rune pulses powerfully.",
            "choices": {
                "l": "Touch the Rune",
                "r": "Ignore and Cross Safely"
            },
            "effects": {
                "l":[["health","add",10],["inventory","reduce","energy",5]],
                "r":[["health","reduce",10],["inventory","reduce","energy",5]]
            }
        },

        "Ignore and Cross Safely": {
            "text":
                "You cross carefully.\n"
                "    The far side leads deeper into old structures.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Touch the Rune": {
            "text":
                "Energy surges through you.\n"
                "    You feel stronger.\n"
                "    A secret staircase appears.",
            "choices": {
                "l": "Secret Staircase",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # Explore Side Tunnel
        # ---------------------------------------------------
        "Explore Side Tunnel": {
            "text":
                "Dim blue moss glows along the walls.\n"
                "    A small pouch of silver lies abandoned on the ground.",
            "choices": {
                "l": "Take the Silver",
                "r": "Move Past Silently"
            },
            "effects": {
                "l":[["inventory","add","silver",7],["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Move Past Silently": {
            "text":
                "You walk quietly forward.\n"
                "    A warm breeze hints at an exit ahead.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Take the Silver": {
            "text":
                "You pocket the silver.\n"
                "    The tunnel bends into a stone courtyard.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # Carved Chamber
        # ---------------------------------------------------
        "Enter Carved Chamber": {
            "text":
                "Intricate carvings fill the walls.\n"
                "    They depict travelers escaping through a radiant Sun Gate.",
            "choices": {
                "l": "Search for Sun Gate",
                "r": "Break a Wall"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5],["health","reduce",5]]
            }
        },

        "Search for Sun Gate": {
            "text":
                "You find the Sun Gate door but lack the key.",
            "choices": {},
            "effects": {}
        },

        "Break a Wall": {
            "text":
                "You smash a weak wall...\n"
                "    Stones collapse instantly.",
            "choices": {},
            "effects": {}
        },

        # ---------------------------------------------------
        # Narrow Crack
        # ---------------------------------------------------
        "Follow Narrow Crack": {
            "text":
                "You squeeze through the narrow gap.\n"
                "    A hidden fresh energy pool lies before you.",
            "choices": {
                "l": "Drink the energy",
                "r": "Fill Bottles"
            },
            "effects": {
                "l":[["health","add",10],["inventory","reduce","energy",5]],
                "r":[["inventory","add","energy",10],["inventory","reduce","energy",5]]
            }
        },

        "Drink the energy": {
            "text":
                "You drink deeply.\n"
                "    The path forward leads into an ancient courtyard.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Fill Bottles": {
            "text":
                "You fill your bottles.\n"
                "    A warm breeze guides you toward an exit.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # Symbol Tunnel
        # ---------------------------------------------------
        "Follow the Symbol Tunnel": {
            "text":
                "Symbols glow brighter as you proceed.\n"
                "    Ahead stands a massive stone door engraved with runes.",
            "choices": {
                "l": "Open the Door",
                "r": "Turn Back"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # Loot Creature
        # ---------------------------------------------------
        "Loot the Creature": {
            "text":
                "Inside the creature's nest you find a shimmering Sun Key.\n"
                "    It radiates a warm golden light.",
            "choices": {
                "l": "Take the Sun Key and Advance",
                "r": "Leave the Key and Retreat"
            },
            "effects": {
                "l":[["inventory","add","key",1],["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Take the Sun Key and Advance": {
            "text":
                "You pocket the Sun Key.\n"
                "    The air vibrates with ancient energy.",
            "choices": {
                "l": "Ancient Gate",
                "r": "Collapsed Corridor"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Leave the Key and Retreat": {
            "text":
                "You step away from the nest.\n"
                "    Darkness grows heavier.",
            "choices": {
                "l": "Collapsed Corridor",
                "r": "Hall of Echoes"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        # ---------------------------------------------------
        # Rest Here
        # ---------------------------------------------------
        "Rest Here": {
            "text":
                "You sit and catch your breath.\n"
                "    Suddenly, a hidden stone panel slides open nearby.",
            "choices": {
                "l": "Enter Hidden Door",
                "r": "Ignore and Move On"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Enter Hidden Door": {
            "text":
                "The hidden chamber is filled with supplies.\n"
                "    You survive here for many years.\n"
                "\n"
                "    ENDING: Survivor — Alive, but never free.",
            "choices": {},
            "effects": {}
        },

        "Ignore and Move On": {
            "text":
                "The path crumbles behind you.\n"
                "    Rubble buries everything.\n"
                "\n"
                "    ENDING: Crushed — A tragic fate.",
            "choices": {},
            "effects": {}
        },

        # ---------------------------------------------------
        # NEW AREAS: Ancient Gate, Collapsed Corridor
        # ---------------------------------------------------
        "Ancient Gate": {
            "text":
                "You reach a towering stone gate.\n"
                "    Symbols swirl around a circular lock.\n"
                "    A depression shaped like a key glows faintly.",
            "choices": {
                "l": "Use Sun Key",
                "r": "Try Forcing the Gate"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["inventory","reduce","energy",5],["health","reduce",5]]
            }
        },

        "Use Sun Key": {
            "text":
                "The key fits perfectly.\n"
                "    The gate blazes with golden light.\n"
                "    A path to freedom opens.",
            "choices": {
                "l": "Step Through the Gate",
                "r": "Look Back One Last Time"
            },
            "effects": {
                "l":[],
                "r":[]
            }
        },

        "Step Through the Gate": {
            "text":
                "You walk through the radiant gate.\n"
                "    Fresh air fills your lungs.\n"
                "\n"
                "    ENDING: Freedom — You escaped the ruins!",
            "choices": {},
            "effects": {}
        },

        "Look Back One Last Time": {
            "text":
                "You turn back and see the ruins fade into darkness.\n"
                "    Then you step into the sunlight.\n"
                "\n"
                "    ENDING: Freedom — You left the past behind.",
            "choices": {},
            "effects": {}
        },

        "Try Forcing the Gate": {
            "text":
                "You push with all your strength.\n"
                "    The stone trembles...\n"
                "    Then collapses on top of you.\n"
                "\n"
                "    ENDING: Crushed — Strength alone was not enough.",
            "choices": {},
            "effects": {}
        },
        # ---------------------------------------------------
        # Collapsed Corridor
        # ---------------------------------------------------
        "Collapsed Corridor": {
            "text":
                "The corridor is unstable.\n"
                "    Rocks fall around you.\n"
                "    A single narrow path leads forward.",
            "choices": {
                "l": "Dash Through",
                "r": "Retreat to Previous Hall"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5],["health","reduce",10]],
                "r":[["inventory","reduce","energy",5]]
            }
        },

        "Dash Through": {
            "text":
                "You sprint through falling debris.\n"
                "    A final doorway glows at the end.",
            "choices": {
                "l": "Open the Door",
                "r": "Collapse From Exhaustion"
            },
            "effects": {
                "l":[["inventory","reduce","energy",5]],
                "r":[["health","reduce",999]]
            }
        },

        "Collapse From Exhaustion": {
            "text":
                "You fall to your knees.\n"
                "    Darkness takes you.\n"
                "\n"
                "    ENDING: Lost Forever — The ruins claim you.",
            "choices": {},
            "effects": {}
        },

        # ---------------------------------------------------
        # Symbol Tunnel ENDINGS
        # ---------------------------------------------------
        "Open the Door": {
            "text":
                "The rune door opens slowly.\n"
                "    Sunlight blinds you.\n"
                "\n"
                "    ENDING: Freedom — You escaped the ruins!",
            "choices": {},
            "effects": {}
        },

        "Turn Back": {
            "text":
                "You wander endlessly.\n"
                "    Thirst overtakes you.\n"
                "\n"
                "    ENDING: Lost Forever — Claimed by the darkness.",
            "choices": {},
            "effects": {}
        },

        # ---------------------------------------------------
        # Leave/Take Key endings (already correct)
        # ---------------------------------------------------
        "Leave the Key and Retreat": {
            "text":
                "Without the key, no door responds to you.\n"
                "    The ruins slowly consume your strength.\n"
                "\n"
                "    ENDING: Trapped — You never escape.",
            "choices": {},
            "effects": {}
        }
    }

    return story_tree.get(location, {})

def show_effects(effects):
    if not effects:
        return
    
    clear()

    WIDTH = 67  
    def center(text):
        return text.center(WIDTH)

    print("\n" * 3)
    print(" " * 4 + "=" * WIDTH)
    print(" " * 4 + center("EFFECT(S) APPLIED"))
    print(" " * 4 + "=" * WIDTH)
    print("\n")

    for e in effects:
        if e[0] == "health":
            action = "Gained" if e[1] == "add" else "Lost"
            amount = e[2]
            line = f"{action} {amount} Health"
            print(" " * 4 + center(line))

        elif e[0] == "inventory":
            action = "Gained" if e[1] == "add" else "Lost"
            item = e[2].capitalize()
            amount = e[3]
            line = f"{action} {amount} {item}"
            print(" " * 4 + center(line))

    print("\n")
    print(" " * 4 + "=" * WIDTH)
    print(" " * 4 + center("Press ENTER to continue"))
    print(" " * 4 + "=" * WIDTH)
    print("\n" * 2)

    input()


def logic(current_location,left_choice,right_choice,left_effect,right_effect,choice_number,inventory):

    user_input = valid_input()
    choice_number += 1

    if user_input == 'l' :
        current_location = left_choice
        for effect in left_effect:
            data_logic(effect)
        show_effects(left_effect)

    elif user_input == 'r' :
        current_location = right_choice
        for effect in right_effect:
            data_logic(effect)
        show_effects(right_effect)

    elif user_input == 'x':
        print("\n    ==== INVENTORY ====")
        for item, qty in GAME_STATE["inventory"].items():
            print(f"    {item.capitalize()} : {qty}")
        print("    ====================")
        print("    ",press_key())  

    else:
        style("Something is Wrong...")

    return(current_location,choice_number)


def ui(current_location,text,left_choice,right_choice,left_effect,right_effect,choice_number,health,inventory):
    '''
    location :                      inventory : {item number} 
    health :                        energy :

    Text : 

    Condition : 

    Enter input : Right, left, x for inventory
    '''
    while True:
    # while True:

        current_health = GAME_STATE["health"]
        current_energy = GAME_STATE["inventory"]["energy"]
        energy_units = max(0, min(10, current_energy // 5))

        print("\n" * 2)
        print("    ========================================================")
        print("                    Entering: ",end='')
        style(f"{current_location:>10}\n")
        print("    ========================================================")
        sleep(1.5)
        clear()

        print(f'''
                        Location : {current_location:>10}

    Health : [{"■" * current_health}{'-' * (10 - current_health)}] {'Energy':>25} :  [{"■" * energy_units}{'-' * (10 - energy_units)}]


    ====================================================================
    
    {text}

    {'':>21}**Choose wisely**

    {'':>12}LEFT :{'':>24}RIGHT :

    {left_choice:>22} {'':<14}{right_choice}
            ''')

        node = story(current_location)

        if not node:
            print("No scene found for : ", current_location)
    
        current_location,choice_number = logic(current_location,left_choice,right_choice,left_effect,right_effect,choice_number,inventory)

        story_data = story(current_location)
        
        node = story(current_location)
        if not node:
            style(f"\n    No scene found for : {current_location}")
            break

        if not story_data["choices"]:
            clear()
            style(story_data["text"], 0.02)
            sleep(2)
            print("\n    Press ENTER to play again...")
            input()
            clear()
            game()
            return

        health = GAME_STATE["health"]
        if health <= 0:
            clear()
            style("\n    YOU HAVE FALLEN...\n")
            sleep(1)
            style("    Your journey ends in darkness.\n")
            sleep(1)
            print("\n    Press ENTER to restart.")
            input()
            clear()
            game()
            return

        inventory = GAME_STATE["inventory"]
        text = story_data["text"]
        left_choice = story_data["choices"]["l"]
        right_choice = story_data["choices"]["r"]
        left_effect = story_data["effects"]["l"]
        right_effect = story_data["effects"]["r"]

        clear()


def game():

        # reset global state
    GAME_STATE["health"] = 10
    GAME_STATE["inventory"] = {
        "energy": 50,
        "silver": 0,
        "gold": 0,
        "key": 0
    }


    current_location = "main"
    choice_number = 0
    health = GAME_STATE["health"]
    inventory = GAME_STATE["inventory"]
    story_data = story(current_location)
    text = story_data["text"]
    left_choice = story_data["choices"]["l"]
    right_choice = story_data["choices"]["r"]
    left_effect = story_data["effects"]["l"]
    right_effect = story_data["effects"]["r"]
    
    ui(current_location,text,left_choice,right_choice,left_effect,right_effect,choice_number,health,inventory) 
    pass

if __name__ == "__main__":

    clear()

    game()
