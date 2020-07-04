class peopleProfile:

    def __init__(self, name, age, SATscore):
        self.name = name
        self.age = age
        self.SATscore = SATscore

    def classify(self):
        if self.age >= 18 and self.SATscore >= 1000:
            return 'Pass'
        else:
            return 'fail'

class club:

    def __init__(self, name, maxParticipants):
        self.name = name
        self.maxParticipants = maxParticipants
        self.participantsList = []

    def addPeople(self, participant):
        if len(self.participantsList) <= self.maxParticipants:
            self.participantsList.append(participant)
            return True
        return False

p1 = peopleProfile('John', 20, 1600)
p2 = peopleProfile('Dan', 21, 1500)
p3 = peopleProfile('Lisa', 20, 1550)

club1 = club("football", 3)

club1.addPeople(p1)
club1.addPeople(p2)
club1.addPeople(p3)

for participant in club1.participantsList:
    print(participant.name)