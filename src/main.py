import csv

# Open the wine_list
with open('wine_list.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')

    # Initialize a counter
    counter = 0
    # loop through each line
    for row in csv_reader:
        # print out the line
        print(row)
        if row[-1] == 'CA':
            counter += 1
    # Print the counter
    print(counter)
