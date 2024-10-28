from datetime import datetime, timedelta


def get_date_range_list(
    start_date: datetime,
    end_date: datetime,
    ):
    return [
        start_date + timedelta(days=n) 
        for n in range((end_date - start_date).days + 1)
    ]
