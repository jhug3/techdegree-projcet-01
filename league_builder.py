#League_builder.py for Project_01 writen by John Hughes 2/9/18

import csv


def make_teams(reader, csv_file):
    # fucntion takes in the reader and csv file. Returns three lists of names, one for each team.
    # Will generate the three lists(teams) based on the height of players and soccer experience.
        # I chose to use height and experience as a method to build the teams.
        # I thought this is what a coach would want to do to make the teams even.
        # Players are seperated into two lists, with and without soccer experience.
        # Then they are sorted by height and split into teams.
    
    exp_yes = []
    exp_no = []
    height_exp = []
    height_no_exp = []
    master_list = []
    for row in reader:
        if (row['Soccer Experience']) == 'YES':
            exp_yes.append(row['Name'])
            height_exp.append(row['Height (inches)'])
        else:
            exp_no.append(row['Name'])
            height_no_exp.append(row['Height (inches)'])
    height_exp.sort()
    height_no_exp.sort()
    csv_file.seek(0)
    # following loop will make a list of names sorted by height with soccer experience.
    for height in height_exp:
        for row in reader:
            if ((row['Height (inches)']) == height) and ((row['Name']) in exp_yes) and (row['Name'] not in master_list):
                master_list.append(row['Name'])
                csv_file.seek(0)
                break
    # following loop will add to the list of names sorted by height, but without soccer experience.
    csv_file.seek(0)
    for height in height_no_exp:
        for row in reader:
            if ((row['Height (inches)']) == height) and ((row['Name']) in exp_no) and (row['Name'] not in master_list):
                master_list.append(row['Name'])
                csv_file.seek(0)
                break            
    #print(master_list) # Used for debugging, verifying the teams are correct.
    # Generating the teams from the master list by slicing the list by 3s.
    sharks_team = [player for player in master_list[::3]]
    dragons_team = [player for player in master_list[1::3]]
    raptors_team = [player for player in master_list[2::3]]
    return sharks_team, dragons_team, raptors_team
    
    
def make_file(reader, csv_file, *teams):
    # Fucntion takes the reader and csv file and three lists of the three teams.
    # Opens a file and writes the teams to the file with formating of:
    # Team name followed by: players name, soccer experience, and guardians name, all on newlines.
    
    sharks, dragons, raptors = teams
    team_names = ['Sharks', 'Dragons', 'Raptors']
    file_name = 'teams.txt' #putting the filename here as a variable, for formating use.
    # Adding in some error checking, did a test by setting the folder to read-only.
    try:
        with open(file_name, 'w',) as csv_wrfile:
            soccer_writer = csv.writer(csv_wrfile)
        #make a writer file must be named teams.txt,
            for team in team_names:
                # print(team) # Used for debugging
                # Setting the list of players to print to the proper teams to the same team name.
                if team == 'Sharks':
                    team_list = sharks
                elif team == 'Dragons':
                    team_list = dragons
                else:
                    team_list = raptors
                soccer_writer.writerow([team])
                for player in team_list:
                    #print(player)  # Used for debugging, printing out the player info.
                    for row in reader:
                        #print(row)  # Used for debugging, printing out the row info.
                        if row['Name'] == player:
                            print_row = row['Name'], ' ' + row['Soccer Experience'], ' ' + row['Guardian Name(s)']
                            soccer_writer.writerow(print_row)
                            csv_file.seek(0)
                            break
    except PermissionError:
        print("Could not write to folder, folder may be read only. Please check that you can write files to this location.")
    print("Your {} file has been created, please check: {}".format('teams', file_name))


def welcome_letters(reader, csv_file, *teams):
    # Function takes the reader and csv file and list of the three teams.
    # Opens and creats 18 files to each player and their guardians.
    # Files incude players name, guardians name, team name, and date of first practice
    # NOTE: this is the extra credit portion!

    sharks, dragons, raptors = teams
    team_names = ['Sharks', 'Dragons', 'Raptors']
    print("Generating 18 letters, each with the players name as the file name:")
    for team in team_names:
        if team == 'Sharks':
            team_list = sharks
        elif team == 'Dragons':
            team_list = dragons
        else:
            team_list = raptors
        for player in team_list:
            for row in reader:
                # The following if staments devide the teams up on seperate practice days.
                if row['Name'] == player and row['Name'] in sharks:
                    first_name, last_name = player.split(' ')
                    player_file_name = first_name.lower() + "_" + last_name.lower() + ".txt"
                    print('Sharks team: ' + player_file_name)
                    # Adding in some error checking, did a test by setting the folder to read-only.
                    try:
                        with open(player_file_name, 'w') as csv_wrfile:
                            letter_writer = csv.writer(csv_wrfile, escapechar=',',  quoting=csv.QUOTE_NONE)
                            print_row = ["Dear " + row['Guardian Name(s)'] + "\n" + row['Name'] + " has been selcected to play on the " + team + ". The first practice will be the first {} of March {}.".format('Monday', '3/1/18')] 
                            letter_writer.writerow(print_row)
                            csv_file.seek(0)
                            break
                    except PermissionError:
                        print("Could not write to folder, folder may be read only. Please check that you can write files to this location.")
                elif row['Name'] == player and row['Name'] in dragons:
                    first_name, last_name = player.split(' ')
                    player_file_name = first_name.lower() + "_" + last_name.lower() + ".txt"
                    print('Dragons team: ' + player_file_name) 
                    # Adding in some error checking, did a test by setting the folder to read-only.
                    try:
                        with open(player_file_name, 'w') as csv_wrfile:
                            letter_writer = csv.writer(csv_wrfile, escapechar=',',  quoting=csv.QUOTE_NONE)
                            print_row = ["Dear " + row['Guardian Name(s)'] + "\n" + row['Name'] + " has been selcected to play on the " + team + ". The first practice will be the first {} of March {}.".format('Tuesday', '3/2/18')] 
                            letter_writer.writerow(print_row)
                            csv_file.seek(0)
                            break
                    except PermissionError:
                        print("Could not write to folder, folder may be read only. Please check that you can write files to this location.")
                elif row['Name'] == player and row['Name'] in raptors:
                    first_name, last_name = player.split(' ')
                    player_file_name = first_name.lower() + "_" + last_name.lower() + ".txt"
                    print('Raptors team: ' + player_file_name) 
                    # Adding in some error checking, did a test by setting the folder to read-only.
                    try:
                        with open(player_file_name, 'w') as csv_wrfile:
                            letter_writer = csv.writer(csv_wrfile, escapechar=',',  quoting=csv.QUOTE_NONE)
                            print_row = ["Dear " + row['Guardian Name(s)'] + "\n" + row['Name'] + " has been selcected to play on the " + team + ". The first practice will be the first {} of March {}.".format('Wednesday', '3/3/18')] 
                            letter_writer.writerow(print_row)
                            csv_file.seek(0)
                            break
                    except PermissionError:
                        print("Could not write to folder, folder may be read only. Please check that you can write files to this location.")
    
    

if __name__ == "__main__":
    # Adding some error checking, will let user know if the csv file can not be found.
    try:
        file_name = 'soccer_players.csv' # putting the file name as a variable here, easy to change.
        with open(file_name, mode='r', newline='') as csv_file:
            soccer_reader = csv.DictReader(csv_file)
            sharks_team, dragons_team, raptors_team = make_teams(soccer_reader, csv_file)
            #print(sharks_team) #for debugging
            #print(dragons_team) #for debugging
            #print(raptors_team) #for debugging
            make_file(soccer_reader, csv_file, sharks_team, dragons_team, raptors_team)
            welcome_letters(soccer_reader, csv_file, sharks_team, dragons_team, raptors_team)
    except FileNotFoundError:
        print("Could not find " + file_name + " please check to be sure it is in the correct directory.")
