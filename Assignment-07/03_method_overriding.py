# Assignment 7 - Program 3
# Method Overriding

class Book:
    def __init__(self, title):
        self.title = title

    def show(self):
        print("Title of Book:", self.title)


class Edition(Book):
    def __init__(self, title, edition):
        super().__init__(title)
        self.edition = edition

    # Method overriding
    def show(self):
        print("Title of Book:", self.title)
        print("Edition:", self.edition)


# Create Edition object
obj = Edition("Python Programming", "Fourth Edition")

# Call overridden method
obj.show()
