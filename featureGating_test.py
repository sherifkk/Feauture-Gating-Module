import unittest
from featureGating import FeatureGating

class FeatureGatingTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(FeatureGating().isAllowed("feature1", ( age > 25 && gender == male ) || salary > 10,000), {
                “age” : 24,
                “gender” : “female”,
                “past_order_amount” : 9000
            }), False)

    def testcase2(self):
        self.assertEqual(FeatureGating().isAllowed("feature2", ( age > 25 && gender == male ) || salary > 10,000), {
                “age” : 25,
                “gender” : “male”,
                “past_order_amount” : 9000
            }), True)

    def testcase3(self):
        self.assertEqual(FeatureGating().isAllowed("feature3", ( age > 25 && gender == male ) || salary > 10,000), {
                “age” : 24,
                “gender” : “female”,
                “past_order_amount” : 11000
            }), True)
