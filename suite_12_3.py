import unittest

import test_12_2
import tests_12_1

runner_tournamentST = unittest.TestSuite()
runner_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runner_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_tournamentST)