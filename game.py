import random

class Country:
    def __init__(self, name, health, military, economy, intelligence, defense, alliances=None, resources=0, happiness=100):
        self.name = name
        self.hp = health  # Stability of the country (e.g., political stability or morale)
        self.military = military  # Military power
        self.economy = economy  # Economic power (GDP)
        self.intelligence = intelligence  # Diplomatic and political influence
        self.defense = defense  # National defense strength
        self.alliances = alliances if alliances else []  # List of allied countries
        self.resources = resources  # Resource reserves (used for economy and military)
        self.happiness = happiness  # Population happiness (affects stability)
    
    def describe(self):
        """Describe the country."""
        return f"{self.name}: HP: {self.hp}, Military: {self.military}, Economy: {self.economy}, Intelligence: {self.intelligence}, Defense: {self.defense}, Resources: {self.resources}, Happiness: {self.happiness}, Alliances: {', '.join(self.alliances)}"

    def attack(self, enemy):
        """Basic attack method for all countries (military strength vs enemy's defense)."""
        damage = self.military - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            return f"{self.name} attacks {enemy.name} for {damage} damage! {enemy.name} has {enemy.hp} HP left."
        else:
            return f"{self.name}'s attack on {enemy.name} was ineffective!"

    def form_alliance(self, other_country):
        """Form an alliance with another country."""
        self.alliances.append(other_country.name)
        other_country.alliances.append(self.name)
        return f"{self.name} and {other_country.name} have formed an alliance!"

    def break_alliance(self, other_country):
        """Break an alliance with another country."""
        self.alliances.remove(other_country.name)
        other_country.alliances.remove(self.name)
        return f"{self.name} and {other_country.name} have broken their alliance."

    def trade(self, other_country, resources_offered, resources_requested):
        """Trade resources with another country."""
        if self.resources >= resources_offered:
            self.resources -= resources_offered
            other_country.resources += resources_offered
            return f"{self.name} trades {resources_offered} resources with {other_country.name}."
        else:
            return f"{self.name} doesn't have enough resources for trade."

    def invest_in_economy(self, amount):
        """Invest in the economy to improve economic power."""
        if self.resources >= amount:
            self.resources -= amount
            self.economy += amount // 2  # Economy grows by half the invested amount
            return f"{self.name} invested {amount} resources into the economy."
        else:
            return f"{self.name} doesn't have enough resources to invest in the economy."

    def manage_happiness(self, policy):
        """Manage population happiness with various policies."""
        if policy == "increase":
            self.happiness += 10
        elif policy == "decrease":
            self.happiness -= 10
        return f"{self.name}'s happiness is now {self.happiness}."

    def experience_world_event(self):
        """Random world events like economic crises, disasters, or booms."""
        event_type = random.choice(["economic_boost", "natural_disaster", "military_crisis", "pandemic", "peace_talks"])
        if event_type == "economic_boost":
            self.economy += 20
            return f"{self.name} experiences an economic boom! Economy increased."
        elif event_type == "natural_disaster":
            self.hp -= 20
            return f"{self.name} suffers a natural disaster! HP decreased."
        elif event_type == "military_crisis":
            self.military += 10
            return f"{self.name} faces a military crisis, boosting military strength."
        elif event_type == "pandemic":
            self.happiness -= 15
            return f"{self.name} is hit by a pandemic. Happiness decreased."
        elif event_type == "peace_talks":
            self.intelligence += 5
            return f"{self.name} successfully leads global peace talks, increasing diplomatic influence."

# Example countries with more attributes and control
usa = Country("United States", health=100, military=90, economy=90, intelligence=85, defense=80, resources=50, happiness=85, alliances=["NATO", "UN"])
china = Country("China", health=100, military=95, economy=85, intelligence=80, defense=85, resources=60, happiness=75, alliances=["BRICS"])
india = Country("India", health=95, military=70, economy=75, intelligence=75, defense=70, resources=45, happiness=80, alliances=["BRICS"])
russia = Country("Russia", health=100, military=85, economy=60, intelligence=80, defense=85, resources=55, happiness=70, alliances=["SCO"])
brazil = Country("Brazil", health=90, military=60, economy=70, intelligence=65, defense=60, resources=50, happiness=80, alliances=["BRICS", "UNASUR"])
germany = Country("Germany", health=100, military=75, economy=95, intelligence=90, defense=80, resources=40, happiness=90, alliances=["EU", "NATO"])

# Example story mode
print("Story Mode: Global Diplomacy and Control")

# Describing countries
print("\nCountry Overview:")
print(usa.describe())
print(china.describe())
print(india.describe())
print(russia.describe())
print(brazil.describe())
print(germany.describe())

# Economic actions
print("\nEconomic Actions:")
print(usa.invest_in_economy(30))  # USA invests in its economy
print(china.trade(usa, 20, 10))  # China trades resources with USA

# Military actions
print("\nMilitary Actions:")
print(usa.attack(russia))  # USA attacks Russia
print(russia.attack(usa))  # Russia counters USA

# Happiness management
print("\nHappiness Management:")
print(usa.manage_happiness("increase"))  # USA increases happiness
print(brazil.manage_happiness("decrease"))  # Brazil decreases happiness

# World events
print("\nWorld Events:")
print(usa.experience_world_event())  # USA experiences a world event
print(germany.experience_world_event())  # Germany experiences a world event

# Diplomacy (forming alliances)
print("\nDiplomatic Actions:")
print(usa.form_alliance(germany))  # USA and Germany form an alliance
print(china.break_alliance(usa))  # China breaks alliance with USA

# Continue the game...
