# JSON config reader. Currently will only be setup to read JSON config files that are created through this program. Would be interesting to make this into a python module at some point to make JSON config's easier to make and manage.
import os
import json

class config_reader():

    def __init__(self, config_path):
        self.config_path = config_path

    def read_config(self, config_section: str, config_key: str):
        try:
            with open(str(self.config_path)) as config:
                config_data = json.load(config)
                data = config_data[f'{config_section}']
                for key, value in data.items():
                    if key == str(config_key):
                        return value
        
        # Check for KeyError as above we need to enter the key EXACTLY as it's written in the config, otherwise python won't know what to find.
        except KeyError:
            print(f"Can't find one or more of the values specified in the config file: {config_section}, {config_key}")
        # We also want to check for AttributeErrors as sometimes I may be dumb and try to loop over a string instead of a dict. haha..haha..
        except AttributeError:
            print("Please check to make sure the values specified in the config aren't strings.")
        except Exception as error:
            print(error)
