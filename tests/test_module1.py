import pytest

from src import main

from .utils import get_assignments, get_calls, get_for_loops, get_ifs

# Task 1
def test_get_call_with_open_module1():
    calls = get_calls(main)
    message = 'Are you calling `open()` and pass in the `wine_list.csv` file?'
    assert 'open:wine_list.csv' in calls, message

# Task 2
def test_import_csv():
    assert 'csv' in dir(main), 'Did you import the csv library?';
# Task 2
def test_csv_reader_is_used():
    calls = get_calls(main)
    message = "Did you call csv.reader? Also make sure you declared the delimiter with delimiter=','"
    assert 'csv:reader:file:delimiter:,' in calls, message

# Task 3
def test_get_loop_for_each_row():
    loops = get_for_loops(main, 'dict')
    message = 'Do you have a `for` loop that loops through the `csv_reader`?'
    assert len(loops) != 0, message

# Task 3
def test_prints_each_row():
    calls = get_calls(main)
    message = 'Do you print each row within the for loop?'
    assert 'print:row' in calls, message

# Task 4
def test_counter_is_assigned():
    assignments = get_assignments(main, return_type='list')
    counter_var = assignments[-1]
    assert counter_var[0] == 'counter', 'Do you initialize a variable named counter?'
    assert int(counter_var[1]) == 0, 'Do you initialize the counter to 0?'

# Task 5
def test_if_is_used():
    ifs = get_ifs(main)
    assert 'row:1:CA:counter:1' in ifs, "Did you write an if block that checks if the last entry of the row is equal to 'CA'"

# Task 7
def test_print_the_counter():
    calls = get_calls(main)
    message = 'Do you print the counter at the end of the for loop?'
    assert 'print:counter' in calls, message

# Task 7
def test_the_counter_is_5():
    assert main.counter == 5
