# from Category import Category

class Transaction:
    def __init__(self, name, value, day, month, year):
        self.name=name
        self.value = value
        self.day = day
        self.month = month
        self.year = year
        self.category = None
        # ist diese Datenstruktur so gut gelöst?

    def add_category(self, category):
        # if not isinstance(category, Category):
        #     raise ValueError("Invalid category...")
        self.category = category

        
