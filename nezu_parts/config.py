def json(self, path: str = 'nezu.json', **kwargs):
    """
    Initialaze nezu via json file
    """
    if self.null:
        import json

        with open(path, 'r', **kwargs) as file:
            all_data = json.load(file)
        nezu_data = all_data.get(self.__id, {})
        self.__seek = nezu_data.get('seek', 0)
        self.__color = nezu_data.get('color', False)