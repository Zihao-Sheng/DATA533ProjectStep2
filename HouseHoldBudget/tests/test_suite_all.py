import unittest

from test_budgetfund_module import TestBudgetFundModule
from test_member_type_module import TestMemberTypeModule
from test_asset_module import TestAssetModule
from test_budget_system_module import TestBudgetSystemModule


def suite():
    loader = unittest.TestLoader()
    s = unittest.TestSuite()

    s.addTests(loader.loadTestsFromTestCase(TestBudgetFundModule))
    s.addTests(loader.loadTestsFromTestCase(TestMemberTypeModule))
    s.addTests(loader.loadTestsFromTestCase(TestAssetModule))
    s.addTests(loader.loadTestsFromTestCase(TestBudgetSystemModule))

    return s


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())