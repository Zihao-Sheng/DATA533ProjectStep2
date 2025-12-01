import unittest
from budget_system.budget_system import BudgetSystem
from budget_system.member.member_type import dependant, guardian


class TestBudgetSystemModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[setUpClass] BudgetSystem tests start")

    @classmethod
    def tearDownClass(cls):
        print("[tearDownClass] BudgetSystem tests end\n")

    def setUp(self):
        self.system = BudgetSystem(
            current_fund=1000,
            address="123 Test St",
            household_name="Test Family",
            members=[]
        )

    def tearDown(self):
        print("[tearDown] Completed one BudgetSystem test")

    def test_member_and_fund_flow(self):
        # Test basic member and fund operations
        self.assertEqual(self.system.household_name, "Test Family")
        self.assertEqual(len(self.system.members), 0)

        d = dependant("Child", "D100", "2015-01-01")
        self.assertTrue(self.system.add_member(d))
        self.assertEqual(len(self.system.members), 1)

        self.system.add_fund(200, "Salary")
        self.system.sub_fund(50, "Snacks")
        self.assertTrue(self.system.validate_fund(1000))

        df = self.system.get_df()
        self.assertGreaterEqual(len(df), 2)

    def test_asset_integration(self):
        # Test linking assets with members
        g = guardian("Parent", "G200", "1980-01-01", income=80000, job_title="Engineer")
        self.system.add_member(g)

        asset = self.system.add_asset_for_member(
            member_id="G200",
            name="Condo",
            asset_type="Real Estate",
            current_value=300000,
            date_acquired="2020-01-01"
        )

        self.assertIsNotNone(asset)
        self.assertEqual(asset.owner, "G200")
        self.assertEqual(len(self.system.property_registry), 1)

        summary = self.system.summarize_assets()
        self.assertIn("Total Value", summary)
        self.assertGreater(summary["Total Value"], 0)