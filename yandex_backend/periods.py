import sys
import datetime


# period_type = sys.stdin.readline().strip()
# start, end = sys.stdin.readline().strip().split()


# WEEK — неделя с понедельника по воскресенье.
# MONTH — месяц.
# QUARTER — интервалы в три месяца: январь — март, апрель — июнь, июль — сентябрь, октябрь — декабрь.
# YEAR — год c 1 января по 31 декабря.
# REVIEW — периоды, за которые оцениваются достижения сотрудников
# Яндекса. Летний период длится с 1 апреля по 30 сентября, зимний — с 1 октября по 31 марта.

class PeriodCreator:

    def __init__(self, period_type, start: datetime.date, end: datetime.date):
        self.end = end
        self.start = start
        self.period_type = period_type
        self.has_end = False

    def get_the_smallest_date(self, date) -> str:
        if self.end <= date:
            self.has_end = True
            return self.end.isoformat()
        return date.isoformat()

    def to_periods(self) -> list:
        if self.period_type == 'WEEK':
            return self.get_weeks()
        elif self.period_type == 'MONTH':
            return self.get_months()
        elif self.period_type == 'QUARTER':
            return self.get_quarter()
        elif self.period_type == 'YEAR':
            return self.get_year()
        elif self.period_type == 'REVIEW':
            return self.get_review()
        else:
            return []

    def get_weeks(self):
        periods = []
        next_end = self.start + datetime.timedelta(days=6 - self.start.weekday())
        periods.append([self.start.isoformat(), self.get_the_smallest_date(next_end)])
        while not self.has_end:
            last_start = next_end + datetime.timedelta(days=1)
            next_end = next_end + datetime.timedelta(days=7)
            periods.append([last_start.isoformat(), self.get_the_smallest_date(next_end)])
        return periods

    def get_months(self):
        periods = []
        next_end = self.start.replace(year=self.start.year + (self.start.month + 1) // 12,
                                      month=(self.start.month + 1) % 12, day=1) - datetime.timedelta(days=1)
        periods.append([self.start.isoformat(), self.get_the_smallest_date(next_end)])
        while not self.has_end:
            last_start = next_end + datetime.timedelta(days=1)
            next_end = last_start.replace(month=(last_start.month + 1) % 12) - datetime.timedelta(days=1)
            periods.append([last_start.isoformat(), self.get_the_smallest_date(next_end)])
        return periods

    def get_year(self):
        periods = []
        next_end = self.start.replace(month=12, day=31)
        periods.append([self.start.isoformat(), self.get_the_smallest_date(next_end)])
        while not self.has_end:
            last_start = next_end + datetime.timedelta(days=1)
            next_end = next_end.replace(year=next_end.year + 1)
            periods.append([last_start.isoformat(), self.get_the_smallest_date(next_end)])
        return periods

    def get_quarter(self):
        periods = []
        if self.start.month in [1, 2, 3]:
            month = 3
        elif self.start.month in [4, 5, 6]:
            month = 6
        elif self.start.month in [7, 8, 9]:
            month = 9
        else:
            month = 12
        next_end = self.start.replace(year=self.start.year + (month + 1) // 12,
                                      month=month + 1, day=1) - datetime.timedelta(days=1)
        periods.append([self.start.isoformat(), self.get_the_smallest_date(next_end)])
        while not self.has_end:
            last_start = next_end + datetime.timedelta(days=1)
            next_end = last_start.replace(year=last_start.year + (next_end.month + 3) // 12,
                                          month=(last_start.month + 3) % 12) - datetime.timedelta(days=1)
            periods.append([last_start.isoformat(), self.get_the_smallest_date(next_end)])
        return periods

    def get_review(self):
        periods = []
        if self.start.month in [4, 5, 6, 7, 8, 9]:
            month = 9
        else:
            month = 3
        next_end = self.start.replace(year=self.start.year + (month + 1) // 12,
                                      month=(month + 1) % 12, day=1) - datetime.timedelta(days=1)
        periods.append([self.start.isoformat(), self.get_the_smallest_date(next_end)])
        while not self.has_end:
            last_start = next_end + datetime.timedelta(days=1)
            next_end = last_start.replace(year=last_start.year + (next_end.month + 6) // 12,
                                          month=(last_start.month + 6) % 12) - datetime.timedelta(days=1)
            periods.append([last_start.isoformat(), self.get_the_smallest_date(next_end)])
        return periods


from pprint import pprint

pprint(PeriodCreator('MONTH', datetime.date.fromisoformat('2020-01-10'),
                    datetime.date.fromisoformat('2020-03-25')).to_periods())
pprint(PeriodCreator('WEEK', datetime.date.fromisoformat('2020-01-26'),
                    datetime.date.fromisoformat('2020-03-23')).to_periods())
pprint(PeriodCreator('REVIEW', datetime.date.fromisoformat('2016-09-20'),
                    datetime.date.fromisoformat('2022-11-30')).to_periods())
pprint(PeriodCreator('QUARTER', datetime.date.fromisoformat('2016-09-20'),
                    datetime.date.fromisoformat('2022-11-30')).to_periods())
pprint(PeriodCreator('YEAR', datetime.date.fromisoformat('2016-09-20'),
                    datetime.date.fromisoformat('2022-11-30')).to_periods())
