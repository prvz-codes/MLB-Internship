# Student Grading System

## Overview

This is a Python-based Student Grading System that allows users to enter a student's details along with their subjects and marks. The program calculates the total obtained marks, percentage, assigns a grade, and displays the final result.

## Features

* Enter student name and class.
* Add multiple subjects dynamically.
* Prevent duplicate subject entries.
* Calculate total obtained marks.
* Calculate overall percentage.
* Assign grades based on percentage.
* Display a formatted result.

## Grade Criteria

| Percentage    | Grade |
| ------------- | ----- |
| 90% and above | A     |
| 80% - 89.99%  | A-    |
| 70% - 79.99%  | B     |
| 60% - 69.99%  | C     |
| 45% - 59.99%  | D     |
| Below 45%     | F     |

## Functions Used

### `calculateAvg()`

Calculates:

* Total obtained marks
* Total marks
* Percentage

Returns:

* Percentage
* Total obtained marks

### `assignGrade()`

Assigns a grade based on the calculated percentage.

### `outputMsg()`

Displays:

* Student information
* Subject-wise obtained marks
* Total obtained marks
* Percentage
* Grade

## How to Run

1. Clone the repository.
2. Navigate to the project folder.
3. Run the program:

```bash
python main.py
```

## Example

```
Enter Student name ? Ali
Enter Student class ? 10

enter subject name : Math
enter total marks of subject ? 100
enter obtained marks of subject ? 92

enter subject name : English
enter total marks of subject ? 100
enter obtained marks of subject ? 84

enter subject name :

Ali YOUR RESULT OF CLASS 10 IS

Math 92.0
English 84.0

GRADE : A-
Total Obtained Marks : 176.0
Percentage : 88.0 %
```

## Concepts Practiced

* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* User Input
* Data Validation
* Modular Programming
