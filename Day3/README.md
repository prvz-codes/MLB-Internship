# Day-3: Persistent Student Record Management System

## Overview

This project is an upgraded version of the Student Record Management System developed on Day-2. It uses **JSON file handling** to permanently store student records, allowing data to persist even after the program is closed.

## Features

* Add Student
* View All Students
* Search Student by Roll Number
* Update Student Information
* Delete Student
* Display Total Number of Students
* Automatic loading of student records at program startup
* Automatic saving of changes to a JSON file
* Input validation using exception handling

## Concepts Used

* File Handling
* JSON (`json.load()` and `json.dump()`)
* Exception Handling (`try-except`)
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements

## What I Learned

* How to read data from a JSON file.
* How to write Python objects to a JSON file.
* How file handling and JSON work together for persistent storage.
* How to use exception handling to prevent program crashes due to invalid input or missing files.
* How to build a console application that stores data permanently.

## Challenges Faced

* Understanding the correct way to update JSON data without corrupting the file.
* Handling missing or empty JSON files.
* Ensuring that every add, update, and delete operation is saved permanently.
* Implementing input validation using exception handling.

## Solution Implemented

* Loaded student records automatically when the program starts.
* Stored student records as a list of dictionaries in a JSON file.
* Created a reusable function to save updated records after every modification.
* Added exception handling for invalid inputs and file-related errors.
* Implemented CRUD operations with persistent storage.

## Conclusion

This project helped me understand Python file handling, JSON data management, and exception handling. It also demonstrated how persistent storage is used in real-world applications to save and retrieve data.
