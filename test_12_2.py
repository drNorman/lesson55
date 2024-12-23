import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, value in all_results.items():
            for i_key, i_value in value.items():
                value[i_key] = str(i_value)
            print(value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        self.tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        global all_results
        temp = self.tournament_1.start()
        all_results[1] = temp
        self.assertTrue(str(temp.get(max(temp.keys()))) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        self.tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        global all_results
        temp = self.tournament_2.start()
        all_results[2] = temp
        self.assertTrue(str(temp.get(max(temp.keys()))) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        self.tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        global all_results
        temp = self.tournament_3.start()
        all_results[3] = temp
        self.assertTrue(str(temp.get(max(temp.keys()))) == 'Ник')


if __name__ == '__main__':
    unittest.main()
