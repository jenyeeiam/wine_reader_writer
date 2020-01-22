import csv

# Open the wine_list
with open('wine_list.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')

    # Initialize a counter
    counter = 0
    # loop through each line
    for line in csv_reader:
        # print out the line
        print(line)
        if line[-1] == 'CA':
            counter += 1

    print("There are {} times the CA is shown".format(counter))
