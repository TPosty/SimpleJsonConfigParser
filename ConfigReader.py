# JSON config reader. Currently will only be setup to read JSON config files that are created through this program. Would be interesting to make this into a python module at some point to make JSON config's easier to make and manage.
import os
import json

class config_reader():

    def __init__(self, config_path):
        self.config_path = config_path

    def create_config(self, config_name: str, *args):
        # Config file name (what to save the file as)
        # Path - Where to save the config file
        
        # First we need to check if a file with that name exists already on the user's OS
        if os.path.exists(os.path.join(self.config_path, config_name)):
            print("Could not create the config due to the file already being there!")
            return
        else:
            # Proceed with the rest of the creation of the config file
            try:
                with open(os.path.join(self.config_path, config_name), 'w') as config:
                    print("Created config file!")
                    # Check if there are other arguments, currently only supports argument for setup data.
                    if args:
                        try:
                            json_data = json.dumps(args[0], ensure_ascii=False, indent=2)
                            config.write(json_data)
                            config.close()
                            print("Found data passed as argument. Wrote data to config file successfully!")
                        except Exception as error:
                            print(error)
                    else:
                        config.write("")
                        config.close()
            except Exception as error:
                print(error)

    def add_section(self, config_path, section_key: str, *args, **kwargs):
        valid_config = False

        if os.path.exists(config_path):
            valid_config = True
        else:
            valid_config = False

        new_data = {
            f"{section_key}": {}
        }
        # First need to make sure that the key is not already inside of the config file
        with open(config_path, 'r+') as config:
            old_config_data = json.load(config)
            print(old_config_data)

            new_config_data = old_config_data | new_data
            
            for key, value in old_config_data.items():
                if section_key == key:
                    print(f"The key: {section_key} is already present!")
                else:
                    print(f"Creating new section: {section_key}")
            
            json_data = json.dump(new_config_data, config)
            print(json_data)
            config.write(json_data)
            print("Wrote new section successfully!")
    
    def remove_section(self, section_name: str):
        pass

    def get(self, config_section: str, config_key: str):
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

config_file_contents = {
    "general": {
        "Username": "Tyler"
    }
}

config = config_reader("C:\\Users\\Owner")

config.create_config("config.json")
config.add_section("C:\\Users\\Owner\\config.json", "about")