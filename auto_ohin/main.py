import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import json
import _jsonnet

from auto_ohin.ohin import ohin


def ohin_from_config(config_path: str) -> None:
    json_str = _jsonnet.evaluate_file(config_path)
    json_dict = json.loads(json_str)

    ohin(**json_dict)


def main():
    import sys
    config_path = sys.argv[1]

    ohin_from_config(config_path)


if __name__ == "__main__":
    import sys
    config_path = sys.argv[1]

    ohin_from_config(config_path)
