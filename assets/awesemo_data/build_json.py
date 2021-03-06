import csv, json, sys, os


def main(arguments):
    player_dict = {}
    # Read projections into a dictionary
    with open('projections.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_dict[row['Name']] = {'Fpts': 'N/A', 'Ownership %': '0', 'Salary': '0', 'Boom %': '0', 'Optimal %': '0', 'Leverage %': '0'}
            player_dict[row['Name']]['Fpts'] = row['Fpts']
            player_dict[row['Name']]['Salary'] = row['Salary']

    # Read ownership into dictionary       
    with open('ownership.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'] in player_dict:
                player_dict[row['Name']]['Ownership %'] = row['Ownership %']

    # Read boom/bust into dictionary
    with open('boom_bust.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'] in player_dict:
                player_dict[row['Name']]['Boom %'] = row['Boom%']
                player_dict[row['Name']]['Optimal %'] = row['Optimal%']
                player_dict[row['Name']]['Leverage %'] = row['Leverage']


    # Store results
    with open('playerData.json', 'w') as fp:
        json.dump(player_dict, fp)


if __name__ == "__main__":
    main(sys.argv)