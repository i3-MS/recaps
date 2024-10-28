from datetime import datetime

from utils.datetime import get_date_range_list
from utils import mapper
from config import config

from .entities import Recap


def get_time_worked_in_minutes(recap: Recap):
    return sum([
        mapper.tdelta_to_minutes(daily.get_time_worked(daily_name))
        for daily_name, daily in recap.dailies.items()
    ])


def get_expected_time(recap: Recap):
    date_range = get_date_range_list(
        recap.date.start,
        recap.date.end,
        )
    return sum([
        recap.get_expected()
        for date in date_range
        if config['weekDays'][date.strftime('%A')]
        and date < datetime.today().date() 
    ])
