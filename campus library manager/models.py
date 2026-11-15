from abc import ABC, abstractmethod

class LibraryItem(ABC):
    total_items = 0  # class attribute, shared by every item
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True              # private
        LibraryItem.total_items += 1         # update the class attribute via the class name

    def is_available(self):
        return self.__available
    
    def mark_borrowed(self):
        self.__available = False

    def mark_returned(self):
        self._available = True

    def __str__(self):
        return f"{self.title} (ID {self.item_id})"
    
    def __repr__(self):
        return f"LibraryItem({self.title}, {self.item_id})"

    @abstractmethod
    def late_fee(self, days_late):
        pass  # every child class must implement this

class Book(LibraryItem):
    DAILY_RATE = 2
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE
    
    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"
    
# TODO: class Magazine(LibraryItem): rate 1, extra field issue_number
class Magazine(LibraryItem):
    DAILY_RATE = 1
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * Magazine.DAILY_RATE
    
    def describe(self):
        return f"Magazine: {self.title}, Issue {self.issue_number} (ID {self.item_id})"
    
# TODO: class DVD(LibraryItem): rate 5, extra field duration_minutes
class DVD(LibraryItem):
    DAILY_RATE = 5
    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * DVD.DAILY_RATE
    
    def describe(self):
        return f"DVD: {self.title}, Duration {self.duration_minutes} mins (ID {self.item_id})"
    
class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []                 # private list of items
    def borrow(self, item):
        # TODO: raise ValueError (with a message) if the item is not available
        if not item.is_available():
            raise ValueError(f"Item '{item.title} (ID {item.item_id})' is not available for borrowing.")
        
        # TODO: raise ValueError (with a message) if the limit is reached
        elif len(self.__borrowed) >= self.max_items:
            raise ValueError(f"Member '{self.name} (ID {self.member_id})' has reached the borrowing limit of {self.max_items} items.")
        
        # TODO: mark the item borrowed and add it to the list
        else:
            item.mark_borrowed()
            self.__borrowed.append(item)
            
        
    def return_item(self, item, days_late=0):
        # TODO: raise ValueError (with a message) if the item is not in the list
        if not item in self.__borrowed:
            raise ValueError(f"Item '{item.title} (ID {item.item_id})' was not borrowed by member '{self.name} (ID {self.member_id})'.")
        else:
        # TODO: mark returned, remove from list, return item.late_fee(days_late)
            item.mark_returned()
            self.__borrowed.remove(item)
            return item.late_fee(days_late)
        
    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]