#!/usr/bin/python3

"""File Storage class
for serialization into a JSON file and
deserialization of JSON file
into an instances.
"""


class FileStorage:

    """
        Private class attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """
