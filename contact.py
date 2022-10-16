"""
Sharon Steinke
Birthday App
"""


class Contact:
    """ creates contact object"""
    def __init__(self):
        self._name = "John Doe"
        self._birthday = "00/00/00"

        self.wishlist = []
        self.pastgifts = []

    @property
    def name(self):
        """gets name"""
        return self._name
    @name.setter
    def name(self, name_):
        """sets name"""
        self._name = name_

    @property
    def birthday(self):
        """gets birthday"""
        return self._birthday
    @birthday.setter
    def birthday(self, birthday_):
        """sets birthday in MM/DD/YYYY format"""
        birthday_list = birthday_.split("/")

        # tests that birthday_ was entered in integers
        for item in birthday_list:
            if item.isdigit() is False:
                error = "Birthday must be entered as positive integers. Formatted MM/DD/YYYY"
                raise Exception(error)

        #tests that birthday_ list has three values (month, day, year)
        if len(birthday_list) < 3 or len(birthday_list) > 3:
            error = """Must be formatted MM/DD/YYYY.
                    Example: 01/01/2000"""
            raise Exception(error)

        #tests appropriate date was entered MM: 1-12, DD: 1-31 depending on month, YY: >= 1900
        month = int(birthday_list[0])
        day = int(birthday_list[1])
        year = int(birthday_list[2])

        if month > 12 or month < 1:
            error = "Month should be a positive integer 1-12"
            raise Exception(error)

        # test year for YYYY format
        if year < 1900 or year > 3000:
            error = """Year must be formatted YYYY.
            It must be between 1900-2999
            Example: 1997"""
            raise Exception(error)

        #tests proper day for February, also tests leap year
        if month == 2:
            if year%4 == 0:
                if day > 29 or day < 1:
                    error = "Day must be a positive integer between 1-29"
                    raise Exception(error)
            elif day > 28 or day <1:
                error = "Day must be a positive integer between 1-28"
                raise Exception(error)

        #tests proper day for 30 day months
        if month in (4, 6, 9, 11):
            if day > 30 or day < 1:
                error = "Day must be a positive integer between 1-30"
                raise Exception(error)

        #tests proper day for 31 day months
        if month in (1, 3, 5, 7, 8, 10, 12):
            if day > 31 or day < 1:
                error = "Day must be a positive integer between 1-31"
                raise Exception(error)

        self._birthday = birthday_
        
    #FIXME:: NEED TO TEST THESE
    def add_wishlist(self, wish):
        """append wish onto the list"""
        self.wishlist.append(wish)
        return self.wishlist

    def remove_wishlist(self, wish):
        """removes specific wish from list"""
        self.wishlist.remove(wish)
        return self.wishlist

