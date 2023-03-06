from Month import Month
from Year import Year
from Transaction import Transaction

class CalenderMonth:
    def __init__(self, month, year, start, end):
        if not isinstance(month, Month):
            raise ValueError("Invalid Month...")
        if not isinstance(year, Year):
            raise ValueError("Invalid Year...")
        self.month = month
        self.year = year
        self.startcapital = start
        self.endcapital = end
        self.members = []
    
    def add_members(self, trnsctn):
        if not isinstance(trnsctn, Transaction):
            raise ValueError("Invalid Transaction...")
        self.members.append(trnsctn)
        #self.save()

class AllCalenderMonths:
    def __init__(self):
        self.members = []
    
    def add_member(self, calendermonth):
        if not isinstance(calendermonth, CalenderMonth):
            raise ValueError("Invalid Calendermont...")
        self.members.append(calendermonth)

    def save(self):
        pass

    def load(self):
        pass

CalenderMonths = AllCalenderMonths()
