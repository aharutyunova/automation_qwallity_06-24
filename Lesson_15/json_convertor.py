import json


class Json_Convertor:
    def json_load(self, filename):
        with open(filename, "r") as f:
            self.load_res = json.load(f)
        return self.load_res

    def json_dump(self, filename):
        with open(filename, "w+") as f:
            json.dump(self.load_res, f, indent=4)
