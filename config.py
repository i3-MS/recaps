import json
from typing import TypedDict


class ConfigWeek(TypedDict):
    Monday: bool
    Tuesday: bool
    Wednesday: bool
    Thursday: bool
    Friday: bool
    Saturday: bool
    Sunday: bool

class Config(TypedDict):
    week: ConfigWeek


with open("config.json", "r") as file:
    config: Config = json.load(file)
