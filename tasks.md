## Purpose of the project
This project will walk you step-by-step to parse a dataset and interpret it. The data is provided by [WineEnthusiast](https://www.winemag.com/?s=&drink_type=wine). Included is a csv file that lists the wine's `country`, `designation`, `price`, `province`, `and variety`. There are formatting errors in the `province` column where California is sometimes printed out in full as `California`, and sometimes abbreviated as `CA`. This is a common problem with datasets where there is no standard practice of data input, or the dataset is modified by different people over time. Your task is to **count how many lines where the province is listed as `CA`.**


## Verify locally
To test this module locally:
* Open up a terminal at the project root
* Run command `pytest`
* This will list all the failing tests.


## Task 1: Open the File

Open the `wine_list.csv` file as a text file with Python's `open()` function.

This process looks something like this
```
with open(<my_file>) as csv_file:
    ## Do stuff with csv_file here
```

## Task 2: Read `csv_file` with the `csv` library `reader` function

Currently we can't do much with the `csv_file` as it is. We need to utilize Python's `csv` module.

At the top of your file import the `csv` library like this.

```
import csv
```

Now we have access to all of the library's functionality. In this project we will be using the `reader` function.

This `reader` function will let us iterate through each line of our data. It will look something like this:
```
with open(<my_file>) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  ## csv_reader is what we can iterate over
```

Note the argument `delimiter=','`. CSV file format stands for "comma separated values". This means that commas separate the data in this particular data set, and we are telling the `reader` function that a `,` indicates the beginning or end of a piece of data.

## Task 3: Print each row of the csv file.
Now that we've read the csv file, let's write a `for` loop to print each row of our data. Iterate over `csv_reader` and use the `print()` function to print each row.

It will look something like this:
```
for row in csv_reader:
  print(row)
```

In your terminal you'll notice that each row is represented by a [list](https://www.tutorialspoint.com/python/python_lists.htm). The first row of the file are the headers, and the province is the last entry of each list.

If you look carefully, you also might notice there are some wines are from `California` but some are listed from `CA`.

## Task 4: Initialize a counter to keep track of how many times we see `CA`

Before the for loop, create a variable `counter` and set it to zero like this:

```
counter = 0
for row in csv_reader:
```

## Task 5: Write an `if` statement.

We only want to increment our counter if the last entry of the list is equal to `CA`. Inside the `for` loop, write an `if` statement to check if the last element of each row is equal to `CA`.

The `index` for the last element of a [list](https://www.tutorialspoint.com/python/python_lists.htm) is `-1`. Your `if` statement will look something like this:

```
if row[-1] == 'CA':
```

## Task 6: Increment the counter inside the `if` block.

Within the `if` block, increment the `counter` by `1`. A shorthand way to increment a variable is with `+= 1`. It will look something like this:

```
counter += 1
```
The `+= 1` is the equivalent of `counter = counter + 1`

## Task 7: Print the total number of `CA`'s in the dataset.

Print the resulting `counter` after the `for` loop like this `print(counter)`. If you've done it right, you should be printing `5`!
