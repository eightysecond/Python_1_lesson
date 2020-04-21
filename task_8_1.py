class Data:
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return f'Текущая дата {Data.extract(self.date)}'

    @classmethod
    def extract(cls, date):
        my_date = []

        for i in date.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f'формат даты введён верно'
                else:
                    return f'не правильно введён год'
            else:
                return f'не правильно введён месяц'
        else:
            return f'не правильно введён день'

    # def __str__(self):
    #     return f'Текущая дата {Data.extract(self.date)}'


today = Data('21 - 04 - 2020')
print(today)
# print(today.extract('21 - 04 - 2020'))
print(Data.extract('21 - 04 - 2020'))
print(today.valid(21, 4, 2020))
print(Data.valid(21, 4, 2021))
