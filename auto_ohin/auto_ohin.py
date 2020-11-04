import json
import _jsonnet

from ohin import ohin


def ohin_from_config(config_path: str) -> None:
    json_str = _jsonnet.evaluate_file(config_path)
    json_dict = json.loads(json_str)

    ohin(**json_dict)


if __name__ == "__main__":
    import sys
    config_path = sys.argv[1]

    ohin_from_config(config_path)
