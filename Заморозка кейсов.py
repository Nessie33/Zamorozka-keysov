from runner import *
from runner_and_tournament import *
import unittest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Усэйн')
        runner.run()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Усэйн')
        runner.walk()
        self.assertEqual(runner.distance, 5)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, Runner("Усэйн"), Runner("Андрей"))
        results = tournament.start()
        self.assertIn(1, results)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, Runner("Ник"), Runner("Джон"))
        results = tournament.start()
        self.assertIn(1, results)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, Runner("Лео"), Runner("Майк"))
        results = tournament.start()
        self.assertIn(1, results)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)