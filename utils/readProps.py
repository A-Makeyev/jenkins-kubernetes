import os
import configparser

base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, '..', 'configuration', 'config.ini')

config = configparser.RawConfigParser()
config.read(config_path)

class ReadConfig():
    @staticmethod
    def getURL():
        return config.get('global data', 'baseURL')

    @staticmethod
    def getStandardUser():
        return config.get('global data', 'standardUser')
    
    @staticmethod
    def getLockedUser():
        return config.get('global data', 'lockedUser')
    
    @staticmethod
    def getInvalidUser():
        return config.get('global data', 'invalidUser')
    
    @staticmethod
    def getPassword():
        return config.get('global data', 'password')