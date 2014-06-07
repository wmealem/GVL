import unittest
import gvl


class TestCMajorCycle2Triad(unittest.TestCase):

    def test_voice_leading_start_on_root(self):
        expected = 'CAGFDCB'
        actual = ''.join(gvl.generate_voice_lead('root'))
        self.assertEqual(expected, actual)

    def test_voice_leading_start_on_fifth(self):
        expected = 'GFECBAF'
        actual = ''.join(gvl.generate_voice_lead('fifth'))
        self.assertEqual(expected, actual)

    def test_voice_leading_start_on_third(self):
        expected = 'EDBAGED'
        actual = ''.join(gvl.generate_voice_lead('third'))
        self.assertEqual(expected, actual)