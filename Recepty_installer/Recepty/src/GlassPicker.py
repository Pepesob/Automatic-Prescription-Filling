import json
import random

_glass_codes = None

def load_glass_codes() -> dict:
    global _glass_codes
    if _glass_codes is None:
        with open("./resources/glass_codes.json", "r", encoding="utf-8") as f:
            _glass_codes = json.load(f)
    return _glass_codes

class GlassPicker:

    def __init__(self):
        self._all_glasses = load_glass_codes()
        self._memory = {}

    
    def pick(self, glass_code: str):
        try:
            self._all_glasses[glass_code]
        except KeyError:
            raise Exception("Unknown code:", glass_code)
        try:
            return self._memory[glass_code]
        except KeyError:
            glass_resource = self._all_glasses[glass_code]
            glasses = glass_resource["glasses"]
            random_glass = random.choice(glasses)
            self._memory[glass_code] = random_glass
            return self._memory[glass_code]

    def pick_id(self, glass_code: str):
        return self.pick(glass_code)["id-prod-handl"]

    def reset(self):
        self._memory = {}


if __name__ == "__main__":

    glass_codes = {'O.01.02.00.D3': '2808927', 'O.01.01.01.B3': '2808963', 'O.01.01.00.B3': '2808934',
                        'O.01.02.01.D.PR': '2632338', 'O.01.01.01.B.PR': '2632574', 'O.01.02.00.D.PR': '2632098',
                        'O.03.01': '2632030', 'O.01.01.00.B.PR': '2632279', 'O.01.02.01.D2.PR': '2632325',
                        'O.01.01.00.B2.PR': '2631965', 'O.01.02.00.D2.PR': '2632457', 'O.01.01.01.B': '2632405',
                        'O.01.02.01.D': '2632765', 'O.01.01.00.B2': '2632660', 'O.01.02.00.D1': '2632536',
                        'O.01.01.01.B1': '2632629', 'O.01.02.01.D1': '2632052', 'O.01.02.00.D': '2632079',
                        'O.01.01.01.B2': '2632809', 'O.01.02.01.D2': '2632459', 'O.01.01.01.B2.PR': '2632187',
                        'O.01.01.00.B1': '2632497', 'O.01.02.00.D2': '2632586', 'O.01.01.00.B': '2632108'}
    
    picker = GlassPicker()
    
    for code, _ in glass_codes.items():
        try:
            print(picker.pick_id(code))
        except Exception as e:
            print(e)

    for code, _ in glass_codes.items():
        try:
            print(picker.pick_id(code))
        except Exception as e:
            print(e)

