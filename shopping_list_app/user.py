"""
    This class adds new user and manages the user's lists
"""
class User(object):
    """ This class manages user's lists"""
    def __init__(self, firstname, secondname, email, password):
        self.firstname = firstname
        self.secondname = secondname
        self.username = firstname +" "+ secondname
        self.email = email
        self.password = password
        self.userlists = {}

    def create_list(self, mylist):
        """Creates a new user list"""
        status = {}
        if mylist.name in self.userlists:
            status.update({"Success":False})
            status.update({"message":"List with same name exists"})
            return status
        status.update({"Success":True})
        status.update({"message":"List added successfully"})
        self.userlists.update({mylist.name: mylist})
        return status
    def delete_list(self, name):
        """deletes a user list"""
        self.userlists.pop(name)
    def update_list(self, name, newlist):
        """updates a user list"""
        self.create_list(newlist)
    def get_list(self, name):
        """gets a specific list"""
        return self.userlists[name]

    def get_all(self):
        """gets all the users lists"""
        return self.userlists
