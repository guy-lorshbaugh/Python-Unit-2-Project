import copy
import constants

teams = constants.TEAMS
players = constants.PLAYERS

def clean_data():
    """Repacks constants.py into a more easily iterated list.  The height value will be an integer, experience values are converted from YES/NO to Booleans, and the guardians value will now be enclosed in a list without 'and.'
    """
    players_copy = copy.deepcopy(players)
    for player in players_copy:
        name = player['name']
        player['height'] = int(player['height'][0:2])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players_copy

cleaned_data = clean_data()

experienced = [
    player for player in cleaned_data if player['experience'] == True
]

inexperienced = [
    player for player in cleaned_data if player['experience'] == False
]

def balance_teams():
    """Sorts players into teams by experience.
    """
    panthers = []
    warriors = []
    bandits = []
    panthers.extend(experienced[0:3] + inexperienced[0:3])
    bandits.extend(experienced[3:6] + inexperienced[3:6])
    warriors.extend(experienced[6::] + inexperienced[6::])
    return panthers, bandits, warriors


def menu():
    """Runs the main menu.
    """
    menu_prompt = None
    while menu_prompt != 2:
        menu_prompt = input(" ---- MENU ----\n - 1. View Team Statistics\n - 2. Quit\n\nYour Selection:  ")
        try:  
            menu_prompt = int(menu_prompt)
        except ValueError:
            print("\n ERROR: Invalid entry.  Please enter a valid numeral.\n")
            continue
        else:
            if not (1 <= menu_prompt <= 2):
                print("\n ERROR: Please enter a valid numeral entry from the list.\n")
                continue
            elif menu_prompt == 2:
                print(f"\n\n{dashes2}\nThank you for using the Basketball Stats Tool!\n{dashes2}\n\n")
                exit()
        team_menu()
    


def team_menu():
    """Runs the team submenu.
    """
    prompt = None
    exp_count = 0
    inexp_count = 0
    while prompt == None:
        prompt = input("\n\nChoose a team to see its roster:\n - 1. Panthers\n - 2. Bandits\n - 3. Warriors\n\nEnter Team Number:  ")
        try:  
            prompt = int(prompt)
        except ValueError:
            print("Invalid entry.  Please enter a valid numeral.\n")
            continue
        else:
            if not (1 <= prompt <= 3):
                print("Please enter a valid numeral entry from the list.\n")
                continue
        teams_list = balance_teams()
        num_players = int(len(players) / len(teams))
        prompt = prompt - 1
        for player in teams_list[prompt]:
            if player['experience'] == True:
                exp_count += 1
            else:
                inexp_count += 1
        list = ", ".join(str(player['name']) for player in teams_list[prompt])
        heights = []
        for player in teams_list[prompt]:
            guards = ", ".join(player['guardians'])
        for player in teams_list[prompt]:
            heights.append(player['height'])
        avg_hgt = sum(heights) / len(heights)
        print(f"\n---- {teams[prompt]} ----".upper())
        print(f"\nTotal players in Team: {num_players}")
        print(f"    - {exp_count} experienced players in team.\n    - {inexp_count} inexperienced players in team.\n")
        print(f"Average Player Height: {avg_hgt}\n")
        print(f"Roster for the {teams[prompt]}:\n", "   ", list, "\n") 
        print("Guardians:")
        print(f"    {guards}\n")
    menu()


if __name__ == '__main__':
    dashes1 = "-" * 38
    dashes2 = "-" * 46
    print(f"\n{dashes1}\nWelcome to the Basketballl Stats Tool!\n{dashes1}\n")
    menu()
