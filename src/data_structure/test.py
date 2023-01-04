from Transaction import Transaction
from DaysOfTheWeek import DaysOfTheWeek

one = Transaction('one', 1, 1, 2023)
two = Transaction('two', 2, 1, 2023)

Doftw = DaysOfTheWeek()

Doftw.which_dotw(one)
Doftw.which_dotw(two)

for weekday in Doftw.weekdays:
    print(weekday.name)
    try:
        print(weekday.members[0].name)
    except:
        pass
