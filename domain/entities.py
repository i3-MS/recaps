from dataclasses import dataclass
from datetime import datetime
from datetime import timedelta


@dataclass
class DailyRecap:
    office: list[str] | None = None
    remote: list[str] | None = None
    tags: list[str] | None = None

    def get_time_worked(self, daily_name: str) -> timedelta:
        FMT = '%H:%M'

        time_worked_office = timedelta(seconds=0)
        time_worked_remote = timedelta(seconds=0)

        if self.office:
            if len(self.office) % 2 == 0:
                for i in range(0, len(self.office), 2):
                    time_worked_remote += (
                        datetime.strptime(self.office[i+1], FMT) - 
                        datetime.strptime(self.office[i], FMT)
                    )
            else:
                print(f'WARNING: {daily_name} {self.office}')
        
        if self.remote:
            if len(self.remote) % 2 == 0:
                for i in range(0, len(self.remote), 2):
                    time_worked_remote += (
                        datetime.strptime(self.remote[i+1], FMT) - 
                        datetime.strptime(self.remote[i], FMT)
                    )
            else:
                print(f'WARNING: {daily_name} {self.remote}')
        
        return time_worked_office + time_worked_remote


@dataclass
class RecapDate:
    start: datetime
    end: datetime


@dataclass
class RecapExpected:
    office_hours: int
    remote_hours: int


@dataclass
class Recap:
    date: RecapDate
    expected: RecapExpected 
    dailies: dict[str, DailyRecap]
    
    def get_expected(self) -> int:
        return (
            self.expected.office_hours + 
            self.expected.remote_hours
        )
