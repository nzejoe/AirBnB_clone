# AirBnB Clone - The Console

## Group Project

- **Language:** Python
- **Paradigm:** Object-Oriented Programming (OOP)
- **By:** Guillaume
- **Weight:** 5
- **Team:** Clergi Clergi, Jonathan Nzete

## Project Timeline

- **Start Date:** Jan 8, 2024, 6:00 AM
- **End Date:** Jan 15, 2024, 6:00 AM
- **Checker Release Date:** Jan 13, 2024, 12:00 PM
- **Manual QA Review:** Must be requested upon project completion
- **Auto Review:** Will be launched at the deadline

## Concepts

For this project, focus on the following concepts:

- Python packages
- AirBnB clone

## Background Context

Welcome to the AirBnB clone project! Before diving into the tasks, please familiarize yourself with the [AirBnB concept page](#).

### First Step: Command Interpreter

The initial step involves building a command interpreter to manage AirBnB objects. This is crucial for laying the foundation for subsequent tasks related to web application development. Key tasks include:

- Implementing a parent class (BaseModel) for initialization, serialization, and deserialization
- Establishing a flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File
- Creating classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel
- Developing the first abstracted storage engine: File storage
- Designing unittests to validate classes and the storage engine

### What’s a Command Interpreter?

Think of it like the Shell but tailored for managing project objects. It should enable actions such as creating new objects, retrieving objects, performing operations on objects, updating object attributes, and destroying objects.

## Resources

Ensure to explore the following resources:

- [cmd module](#)
- [cmd module in depth](#)
- [Packages concept page](#)
- [uuid module](#)
- [datetime](#)
- [unittest module](#)
- [args/kwargs](#)
- [Python test cheatsheet](#)
- [cmd module wiki page](#)
- [Python unittest](#)

## Learning Objectives

By the end of this project, you should be able to explain:

### General

- How to create a Python package
- How to create a command interpreter using the cmd module
- Understanding Unit testing and implementing it in a large project
- Serialization and deserialization of a Class
- Reading and writing JSON files
- Managing datetime
- Understanding UUID
- Utilizing *args and **kwargs
- Handling named arguments in a function

### Copyright - Plagiarism

- Develop solutions independently to meet learning objectives
- Strictly avoid plagiarism, which may result in removal from the program
- Do not publish any content related to this project

## Requirements

### Python Scripts

- Editors: vi, vim, emacs
- Interpretation/Compilation: Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files end with a new line
- First line: `#!/usr/bin/python3`
- Mandatory README.md file at the project's root
- Code follows pycodestyle (version 2.8.*)
- All files must be executable
- Length of files tested using `wc`
- Modules, classes, and functions have documentation
- Documentation is a complete sentence explaining the purpose
- Unit tests organized in the `tests` folder
- Unittest module used for tests
- Test files start with `test_`
- Test file organization mirrors project structure
- Tests executed with `python3 -m unittest discover tests`

### GitHub

- One project repository per group
- Cloning/forking a repository with the same name before the second deadline risks a 0% score.
