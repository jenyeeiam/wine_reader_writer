## Purpose of the project
This project will provide you a step-by-step guide clean a dataset of wine reviews from WineEnthusiast(https://www.winemag.com/?s=&drink_type=wine). Included is a csv file that lists the wine's country, designation, price, province, and variety. There are formatting errors in the province column where California is sometimes printed out in full as `California` and sometimes abbreviated as `CA`. This is a common problem with datasets where the standard of data input is not enforced. Your task is standardize the province column to replace all the entries of `CA` with `California`, then return a clean csv file.


## Verify locally
To test this module locally:
* Open up a terminal at the project root
* Run command `pytest`
* Everything should be green!


## Task 1 Print the Data: Open the `wine_list.csv` file as a text file with Python's `open()` function. Then, pass the file to the csv library's `reader` function. Print each line of the file.

A sample input file named `wine_list.csv` is provided as part of the project.
We need to open it to get a [file object](https://docs.python.org/3.7/glossary.html#term-file-object) using the [open() method](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

This process looks something like this
```
with expression as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Write a for loop here, iterating through each line of csv_reader and print each line
```

In above structure, use `open()` in the `expression`, and name the variable as `infile`.


## Task 2: Loop through each line in `infile`
With the `infile` variable, we can loop through it to get each line in the `input.txt` file.

A simple way is just loop through the `infile` file object.
The basic structure of a loop in Python is as such:
```
for variable in iterable:
    body
```

Add a line of `for`-loop where the varible is named `line` and the iterable is `infile`.

The following tasks will fill in the `body` part of the loop


## Task 3: Separate line into list
Note that the fields in each line is separated by a space (`' '`) in `input.txt`.
For example, the first line is:
```
answer 42
```

Using the [str.split()](https://docs.python.org/3.7/library/stdtypes.html#str.split) function, split the `line` into a variable named `splitted`, with separator of a space.


## Task 4: Get the last element in the splitted list
Once we get the `splitted` list, it's time to get the last element in it.

To get the element at a given `index` in a `list`, use the following syntax: `list`[`index`], then assign it to a variable named `last`.

The `index` for the last element is `-1`.

## Task 5: Cast `last` into an int
Since we know for sure the last element is an integer, it's good practice to cast it to an integer (e.g. for comparison with another integer).

The build-in function [`int()`](https://docs.python.org/3.7/library/functions.html#int) can be used for such casting.

Store the casting result into a variable named `value`.


## Task 6: Print out the value
Finally, we get the integer of each line in the input file.
It's time to print it out.

Print the result `value` using the [`print()`](https://docs.python.org/3.7/library/functions.html#print) build-in function.
