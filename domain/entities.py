from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta


@dataclass
class DailyRecap:
    offline: list[str] | None = None
    remote: list[str] | None = None
    tags: list[str] | None = None

    def get_time_worked(self) -> timedelta:
        FMT = '%H:%M'

        time_worked_offline = timedelta(seconds=0)
        time_worked_remote = timedelta(seconds=0)

        if self.offline and len(self.offline) == 2:
            time_worked_offline = (
                datetime.strptime(self.offline[1], FMT) - 
                datetime.strptime(self.offline[0], FMT)
            )

        if self.remote and len(self.remote) == 2:
            time_worked_remote = (
                datetime.strptime(self.remote[1], FMT) - 
                datetime.strptime(self.remote[0], FMT)
            )
        
        return time_worked_offline + time_worked_remote


@dataclass
class RecapDate:
    start: datetime
    end: datetime


@dataclass
class RecapExpected:
    offline_hours: int
    remote_hours: int


@dataclass
class Recap:
    date: RecapDate
    expected: RecapExpected 
    dailies: dict[str, DailyRecap]
    
    def get_expected(self) -> int:
        return (
            self.expected.offline_hours + 
            self.expected.remote_hours
        )
