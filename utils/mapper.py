from datetime import timedelta
from typing import Type, Any, TypeVar
from dataclasses import is_dataclass, fields


T = TypeVar("T")


def dict_to_dataclass(
    dataclass: Type[T] | str,
    data: Any,
    ) -> T:
    if is_dataclass(dataclass) and isinstance(data, dict):
        dictionary: dict[str, Any] = data

        field_types = {
            f.name: f.type for f in fields(dataclass)
        }
        return dataclass(**{
            key: dict_to_dataclass(field_types[key], dictionary[key])
            for key in dictionary if key in field_types
        })
    return data


def tdelta_to_minutes(tdelta: timedelta):
    return tdelta.total_seconds() / 60


def minutes_to_decimal_hours(minutes: float):
    if minutes == 0:
        return 0
    return minutes / 60


def decimal_hours_to_hours(decimal_hours: float):
    sign = '-' if decimal_hours < 0 else ''
    decimal_hours = abs(decimal_hours)

    hours = int(decimal_hours)
    minutes = (decimal_hours * 60) % 60
    return "%s%d:%02d" % (sign, hours, minutes)
