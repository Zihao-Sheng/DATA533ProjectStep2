import unittest
from budget_system.member.member_type import dependant, guardian


class TestMemberTypeModule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[setUpClass] MemberType tests start")

    @classmethod
    def tearDownClass(cls):
        print("[tearDownClass] MemberType tests end\n")

    def setUp(self):
        self.dep = dependant("Child", "D001", "2015-01-01")
        self.guard = guardian("Parent", "G001", "1980-01-01", income=50000, job_title="Teacher")

    def tearDown(self):
        print("[tearDown] Completed one MemberType test")

    def test_dependant_basic(self):
        # Test dependant attributes and updates
        self.assertEqual(self.dep.name, "Child")
        self.assertEqual(self.dep.ID, "D001")
        self.assertEqual(self.dep.type, "dependant")

        self.dep.new_name("New Child")
        self.dep.new_ID("D001-X")
        self.dep.new_DOB("2016-02-02")

        self.assertEqual(self.dep.name, "New Child")
        self.assertEqual(self.dep.ID, "D001-X")
        self.assertEqual(self.dep.DOB, "2016-02-02")

        s = str(self.dep)
        self.assertIn("New Child", s)

    def test_guardian_job_and_income(self):
        # Test guardian job and income behavior
        self.assertEqual(self.guard.job_title, "Teacher")
        self.assertEqual(self.guard.income, 50000)

        self.guard.new_job("Engineer")
        self.guard.new_income(80000)

        self.assertEqual(self.guard.job_title, "Engineer")
        self.assertEqual(self.guard.get_income(), 80000)

        s = str(self.guard)
        self.assertIn("Engineer", s)