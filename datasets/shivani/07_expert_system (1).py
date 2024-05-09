class ExpertSystem:
    def __init__(self):
        self.rules = {}  

    def add_rule(self, condition, action):
        self.rules[condition] = action

    def infer(self, condition):
        if condition in self.rules:
            return self.rules[condition]
        else:
            return "No action specified for this condition."

expert_system = ExpertSystem()


expert_system.add_rule("sunny", "play tennis")
expert_system.add_rule("rainy", "stay indoors")


print(expert_system.infer("sunny"))  
print(expert_system.infer("rainy"))  
print(expert_system.infer("cloudy"))  
