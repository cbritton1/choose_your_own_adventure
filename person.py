class Person:
    name = ''
    decision = ''
    matches = 0
    file = 'begin'

    def __init__(self, name):
        self.name = name
        self.matches = 3

    def set_decision(self, decision):
        self.decision = decision

    def set_name(self, name):
        self.name = name

    def use_match(self):
        print("You use a match\n")
        self.matches = self.matches - 1

    def set_matches_zero(self):
        self.matches = 0
