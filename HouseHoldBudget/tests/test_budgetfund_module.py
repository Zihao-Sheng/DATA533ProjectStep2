import unittest
from budget_system.budgetfund.budgetfund import budgetfund

class TestBudgetFundModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[setUpClass] TestBudgetFundModule")

    @classmethod
    def tearDownClass(cls):
        print("[tearDownClass] TestBudgetFundModule\n")

    def setUp(self):
        self.fund=budgetfund(opening_balance=1000, name='Test Household')

    def tearDown(self):
        print("[tearDown] Finished one TestBudgetFundModule test method")

    def test_add_and_sub(self):
        #testing opening balance
        self.assertEqual(self.fund.get(),1000.0)
        #testing adding balance
        result_add=self.fund.add(200,'Salary')
        self.assertTrue(result_add)
        self.assertEqual(self.fund.get(),1200.0)
        #testing subtracting balance
        result_add=self.fund.sub(300,'Grocery')
        self.assertTrue(result_add)
        self.assertEqual(self.fund.get(),900.0)
        #testing log length
        df=self.fund.get_log()
        self.assertEqual(len(df),2)

    def test_validate_and_failed_transaction(self):
        # testing if there is sufficient fund
        self.assertTrue(self.fund.validate(500))
        # testing when there is not sufficient fund
        self.assertFalse(self.fund.validate(5000))
        # testing if the fund will get deducted if fund in sufficient
        result = self.fund.sub(5000, "Big Purchase")
        self.assertFalse(result)
        self.assertEqual(self.fund.get(), 1000.0)
        # checking if the log has failed record
        df = self.fund.get_df()
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["status"], "failed")