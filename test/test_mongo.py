import unittest
import sys
sys.path.insert(0, 'src')
from tools import *
from testers import *


class MongoauditTest(unittest.TestCase):

    def create_type(self, **kwargs):
        return type("mock", (object,), kwargs)

    def info_obj(self, info):
        return self.create_type(tester=self.create_type(info=info))

    def ver_obj(self, ver):
        return self.info_obj({"version": ver})


    def test_alert1(self):
        self.assertFalse(alerts_dec012015(self.info_obj({"version": "3.0.3", "modules":["enterprise"]})))

    def test_alert1_1(self):
        self.assertTrue(alerts_dec012015(self.info_obj({"version": "3.0.2", "modules":["rock"]})))

    def test_alert2(self):
        self.assertFalse(alerts_mar272015(self.ver_obj("3.0.0")))

    def test_alert3(self):
        self.assertFalse(alerts_mar252015(self.ver_obj("2.4.0")))

    def test_alert4(self):
        self.assertFalse(alerts_feb252015(self.ver_obj("2.6.0")))

    def test_alert5(self):
        self.assertFalse(alerts_jun172014(self.ver_obj("2.6.0")))

    def test_alert6(self):
        self.assertFalse(alerts_may052014(self.ver_obj("2.6.0")))

    def test_alert7(self):
        self.assertFalse(alerts_jun202013(self.ver_obj("2.4.2")))

    def test_alert8(self):
        self.assertFalse(alerts_jun052013(self.ver_obj("2.4.4")))
