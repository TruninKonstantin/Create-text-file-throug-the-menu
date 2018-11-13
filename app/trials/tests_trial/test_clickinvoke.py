import unittest

import app.trials.clickinvoke as clickinvoke


class TestClickInvoke(unittest.TestCase):
    def setUp(self):
        self.app = clickinvoke.ClickInvoke()

    def tearDown(self):
        self.app.destroy()

    def test_button1(self):
        self.app.children['b1'].invoke()

    def test_button2(self):
        self.app.children['b2'].invoke()