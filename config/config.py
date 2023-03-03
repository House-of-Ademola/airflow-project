from configparser import ConfigParser
from pathlib import Path


def get_project_root() -> Path:  # Returns project root folder
    return Path(__file__).parents[1]


def config(config_db):
    section = 'postgresql'
    config_file_path = 'config' + config_db
    if len(config_file_path) > 0 and len(section) > 0:
        config_parser = ConfigParser()  # Create an instance of ConfigParser class
        config_parser.read(config_file_path)  # Read the configuration file
        if config_parser.has_section(section):  # If the configuration file contains the provided section name
            config_params = config_parser.items(section)  # Read the options of the section
            db_conn_dict = {}  # Convert the list object to a python dictionary object & define an empty dictionary
            for config_param in config_params:  # Loop in the list
                key = config_param[0]  # Get the key
                value = config_param[1]  # Get the value
                db_conn_dict[key] = value  # Add the key value pair in the dictionary object
            return db_conn_dict  # Get connection object use above dictionary object
