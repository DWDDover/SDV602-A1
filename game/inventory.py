class Inventory:
    def __init__(self):
        self.items = []

    def has_item(self, item):
        return item in self.items
    
    def get_item_by_name(self, name):
        #method to help parse use and equip player input
        name = name.lower()
        for item in self.items:
            if item.name.lower() == name:
                return item
        return None

    def add_item(self, item):
        if not self.has_item(item):
            self.items.append(item)
            return True

        return False
