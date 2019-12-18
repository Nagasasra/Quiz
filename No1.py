class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + "\n" + self.get_description() #missing proper quotation marks for strings

    def get_description(self):
        return "Nodescription" # it says statement seem to have no effect, changing it with proper quotation marks fixed it

    def execute(self):
        print(self.incantation) # need to be inside brackets

    def study_spell(spell):
        print(spell)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self,'Accio', 'Summoning Charm') # again, wrong quotation marks for strings
class Confundo(Spell): # this line was over-indented, fixed it with proper indentation
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'ConfundusCharm')
    def get_description(self):
        return'Causes the victim to become confused and befuddled.' #wrong quoatation marks



spell = Accio()
spell.execute()
spell.study_spell()
Confundo.study_spell(Confundo())

# a. Parent class is Spell, child classes are Accio and Confundo
# b. Accio Summoning Charm Accio Nodescription ConfundusCharm Confundo Causes the victim to become confused and befuddled.
# c. since it calls Confundo class, it would be the method get_description() inside Confundo class
# d. str function, might also work with repr
