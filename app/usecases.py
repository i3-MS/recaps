from domain.entities import Recap
from domain import services
from adapters.gateways import RecapGateway
from adapters.mapper import RecapMapper
from utils import mapper


def _print_details_by_time_values(
    time_expected_in_decimal_hours: int,
    time_worked_in_minutes: float,
    type: str,
    ):
    time_worked_in_decimal_hours = mapper.minutes_to_decimal_hours(time_worked_in_minutes)
    time_worked_in_hours = mapper.decimal_hours_to_hours(time_worked_in_decimal_hours)
    time_worked_diff_in_hours = mapper.decimal_hours_to_hours(
        time_worked_in_decimal_hours - time_expected_in_decimal_hours)
    
    print()
    print(type)
    print('time_expected_in_decimal_hours:', time_expected_in_decimal_hours)
    print('time_worked_in_minutes:', time_worked_in_minutes)
    print('time_worked_in_decimal_hours:', time_worked_in_decimal_hours)
    print('time_worked_in_hours:', time_worked_in_hours)
    print('time_worked_diff_in_hours:', 
        (f'{"+" if not time_worked_diff_in_hours.startswith("-")else ""}'
         f'{time_worked_diff_in_hours}'))


def print_recap_details(recap_path: str) -> Recap | None:
    recap_dict = RecapGateway.load(recap_path)
    if recap_dict is None:
        return None

    recap = RecapMapper.dict_to_domain(recap_dict)

    time_expected_in_decimal_hours = services.get_total_expected_time(recap)
    time_worked_in_minutes = services.get_time_worked_in_minutes(recap)
    _print_details_by_time_values(
        time_expected_in_decimal_hours, 
        time_worked_in_minutes,
        type='[total]')
    
    time_expected_in_decimal_hours = services.get_total_expected_time(recap, type='office')
    time_worked_in_minutes = services.get_time_worked_in_minutes(recap, type='office')
    _print_details_by_time_values(
        time_expected_in_decimal_hours, 
        time_worked_in_minutes,
        type='[office]')
    
    time_expected_in_decimal_hours = services.get_total_expected_time(recap, type='remote')
    time_worked_in_minutes = services.get_time_worked_in_minutes(recap, type='remote')
    _print_details_by_time_values(
        time_expected_in_decimal_hours, 
        time_worked_in_minutes,
        type='[remote]')

    return recap
