import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        anny_1 = Runner('Anny_1')
        for i in range(10):
            anny_1.walk()
        self.assertEqual(anny_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        anny_2 = Runner('Anny_2')
        for i in range(10):
            anny_2.run()
        self.assertEqual(anny_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        anny_3 = Runner('Anny_3')
        anny_4 = Runner('Anny_4')
        for i in range(10):
            anny_3.run()
            anny_4.walk()
        self.assertNotEqual(anny_3.distance, anny_4.distance)


if __name__ == "__main__":
    unittest.main()
