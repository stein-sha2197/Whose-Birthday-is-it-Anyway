"""
Sharon Steinke
Who's Birthday is it Anyway?


"""

class User:
    """
    creates user object with user's name, email, phone number, user name, and password
    can update info.
    """
    def __init__(self, first, last, phone, email, birthday, user, password):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.user = user
        self.password = password
    def change_phone(self):
        pass
    def change_email(self):
        pass
    def change_user(self):
        pass
    def change_password(self):
        pass
    def forgot_password(self):
        pass

class Contact:
    """
    creates a contact object
    """
    contacts = 0
    def __init__(self, first, last, birthday):
        self.first = first
        self.last = last
        self.pronoun = pronoun
        self.birthday = birthday

        contacts += 1
    def add_pronoun(self):
        "add or change pronouns"
        pass
    def add_photo(self):
        """adds a contact photo"""
        pass
    def add_phone(self):
        """add or change phone number"""
        pass
    def add_email(self):
        """add or change email"""
        pass
    def add_address(self):
        """add or change address"""
        pass
    def add_previousgift(self):
        """adds to a list. Can edit list"""
        pass
    def add_wishlist(self):
        """adds to a list. Can edit list"""
        pass
    def add_favorite(self):
        """adds to a list. Can edit list"""
        pass
    def add_reminder(self):
        """adds when user would like to be
        reminded about this contacts birthday"""
        pass
def sign_in(user,password):
    """sign in to app"""
    pass
def create_user():
    """creates user object"""
    pass

def mainmenu(select):
    """add contact, update wishlist, search contacts"""
    pass

def add_contact(first, last, birthday):
    """creates contact object"""
    pass

def update_wish(contact, wish):
    """add a wish to wish list"""
    pass

def search_contacts(string):
    """searches file of saved contacts and returns the results"""
    pass
    
def send_reminder(contact):
    """sends reminder of contact's birthday to user based on user
    preference"""
    pass

def update_contactbook(contact):
    """updates a file with contact object"""
    pass

def main():
    """runs the program"""
    pass


if __name__ == "__main__":
    main()
