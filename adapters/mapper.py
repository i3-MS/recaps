from domain.entities import (
    Recap, 
    RecapDate, 
    RecapExpected, 
    DailyRecap,
)


class RecapMapper:

    @staticmethod
    def dict_to_domain(recap_dict: dict) -> Recap:
        recap_expected = RecapExpected(
            offline_hours=recap_dict['expected']['offline_hours'],
            remote_hours=recap_dict['expected']['remote_hours'],
        )
        recap_date = RecapDate(
            start=recap_dict['date']['start'],
            end=recap_dict['date']['end'],
        )
        recap_dailes = {
            str(recap_name): DailyRecap(
                offline=recap_data.get('offline', None),
                remote=recap_data.get('remote', None),
                tags=recap_data.get('tags', None),
            )
            for recap_name, recap_data in recap_dict['dailies'].items()
        }
        return Recap(
            date=recap_date,
            expected=recap_expected,
            dailies=recap_dailes,
        )
