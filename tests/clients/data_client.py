import json

class DataClient:
    def __init__(self) -> None:
        self.path_to_file = "tests/data/test_data.json"
        
    def write_playload(self, playload, key='created'):
        read_data = self.__read_data()
        read_data[key].append(playload)
        with open(self.path_to_file, 'r+') as file:
            file.write(json.dumps(
              read_data, indent=4
            ))
        
    def get_fixture_data(self, key, amount_var):
        data = self.__read_data()[key] 
        list = [tuple(data[i:i + amount_var]) for i in range(0, len(data), amount_var)]
        return list
    
    def get_regular_data(self, key):
        data = self.__read_data()[key] 
        return data
    
    def __read_data(self):
        with open(self.path_to_file, 'r') as file:
            data = json.load(file)
        return data 