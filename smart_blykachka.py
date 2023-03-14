"""Classes"""
class Region:
    """
    Create values
    """
    def __init__(self, name):
        self.name = name
        self.lst = {}
        self.description = ""
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description
    
    def link_room(self, room, destination):
        self.lst[destination] = room

    def get_description(self):
        return self.description
    
    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def get_details(self):
        print("Ти прибув у %s" %(self.name))
        print(self.description)
        for element in self.lst:
            room = self.lst[element]
            print("%s на %s."  %(room.get_name(),  element))
        
    def move(self, element):
        if element in self.lst:
            return self.lst[element]
        else:
            print("Сюди не пройти")
            return self
class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sensation = ""
        self.subject = None
        self.item = None
        self.defeated = 0
    
    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        print(self.conversation)

    def get_name(self):
        return self.name
    
    def set_item(self, item):
        self.item = item

    def describe(self): 
        print(f'Ух ти, хтось спостерігає за тобою.')
        print(self.description)

class Enemy(Character):
    defeated = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.sensation = ""
        self.subject = None
        self.item = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        print(self.conversation)

    def fight(self, subject):
        if subject == self.subject:
            Enemy.defeated += 1 
            print("Ти відбив %s за допомогою %s" %(self.name, self.subject))
            return True
        else:
            print("%s покалічив тебе, негідник!" %(self.name))
            return False

    def set_weakness(self, subject):
        self.subject = subject

    def get_weakness(self):
        return self.subject

    def get_name(self):
        return self.name
    
    def get_defeated(self):
        return self.defeated
    
    def describe(self): 
        print(f'Обережно, {self.name} спостерігає за тобою!')
        print(self.description)

class Item:
    def __init__(self, product):
        self.product = product
        self.description = ""
    
    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.product
    
    def describe(self):
        if self.product is not None:
            print("Оо, тобі трапилась %s" %(self.get_name()))
        print(self.description)
