import unittest
import gvl


class TestCMajorCycle2Triad(unittest.TestCase):

    def test_voice_leading_start_on_root(self):
        expected = ['C', 'A', 'G', 'F', 'D', 'C', 'B']
        actual = gvl.generate_voice_lead('C major',
                                         'cycle2',
                                         'root')
        self.assertEqual(expected, actual)

    def test_voice_leading_start_on_fifth(self):
        expected = ['G', 'F', 'E', 'C', 'B', 'A', 'F']
        actual = gvl.generate_voice_lead('C major',
                                         'cycle2',
                                         'fifth')
        self.assertEqual(expected, actual)

    def test_voice_leading_start_on_third(self):
        expected = ['E', 'D', 'B', 'A', 'G', 'E', 'D']
        actual = gvl.generate_voice_lead('C major',
                                         'cycle2',
                                         'third')
        self.assertEqual(expected, actual)


class TestCHarmonicMinorCycle2Triad(unittest.TestCase):

    def test_voice_leading_starting_on_root(self):
        expected = ['C', 'A♭', 'G', 'F', 'D', 'C', 'B']
        actual = gvl.generate_voice_lead('C harmonic minor',
                                         'cycle2',
                                         'root')
        self.assertEqual(expected, actual)
