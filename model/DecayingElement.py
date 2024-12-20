from model.DecayType import DecayType
from model.Element import Element

class DecayingElement(Element):
    def __init__(self, symbol, atomic_number, atomic_weight, possible_decays, half_life):
        
        # The name and category of the element is not important for the decaying element so just set them to random values
        self.name = "Decaying Element" 
        super().__init__(symbol, self.name, atomic_number, atomic_weight, "None")
        
        # possible decays should be a dictionnary with this structure:
        # {decay_type: child isotope}
        # example: {"alpha": "He"}
        # example: {"beta-": "B"}
        # example: {"beta+": "C"}
        self.possible_decays:dict[DecayType, DecayingElement] = possible_decays
        
        self.half_life = half_life
        
    def decay(self, decay_type):
        if decay_type in self.possible_decays:
            self.fetchDecayingElementData(self.possible_decays[decay_type])
        else:
            print(f"Decay type {decay_type} not possible for {self.symbol}")
            
    def fetchDecayingElementData(self, symbol):
        # fetch data from json
        pass
    # for debugging purposes
    def helloWorld(self):
        print("Hello World! I am " + self.symbol + " and I am a Decaying Element!" + " I can decay into " + str(self.possible_decays))
        
    def printDecayers(self):
        for value in self.possible_decays.values():
            value.helloWorld()
            value.printDecayers()
