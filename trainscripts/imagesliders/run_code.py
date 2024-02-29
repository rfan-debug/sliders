import json

from prompt_util import load_prompts_from_yaml

if __name__ == "__main__":
    ss = load_prompts_from_yaml(
        "./data/prompts-xl-weather.yaml",
        attributes=[
            "cold",
            "warm",
        ]
    )
    print("-----")
    print(ss)
