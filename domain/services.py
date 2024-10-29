from datetime import datetime

from utils.datetime import get_date_range_list
from utils import mapper
from config import config

from .entities import Recap


def get_time_worked_in_minutes(recap: Recap, type: str | None = None):
    result = 0
    for daily_name, daily in recap.dailies.items():
        time_worked_office, time_worked_remote = daily.get_time_worked(daily_name)
        if not type or type == 'office':
            result += mapper.tdelta_to_minutes(time_worked_office)
        if not type or type == 'remote':
            result += mapper.tdelta_to_minutes(time_worked_remote)
    return result


def get_total_expected_time(recap: Recap, type: str | None = None):
    date_range = get_date_range_list(
        recap.date.start,
        recap.date.end,
        )
    
    value_by_type = {
        'office': recap.expected.office_hours,
        'remote': recap.expected.remote_hours,
        None: recap.get_expected_total(),
    }
    
    result = 0

    for date in date_range:
        if (config['weekDays'][date.strftime('%A')]
            and date < datetime.today().date()
            ):
            result += value_by_type.get(type, 0)

    return result
