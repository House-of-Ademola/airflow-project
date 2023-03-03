from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()  # Create a parser
