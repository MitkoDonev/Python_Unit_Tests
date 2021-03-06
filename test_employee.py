from unittest import TestCase
from unittest.mock import patch
from employee import Employee


class TestEmployee(TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup Class")

    @classmethod
    def tearDownClass(cls):
        print("Teardown Class")

    def setUp(self):
        print("Create Object Instanse")
        self.employee1 = Employee("Corey", "Schafer", 50000.50)
        self.employee2 = Employee("Sue", "Smith", 60000.90)

    def tearDown(self):
        print("Tear Down")

    def test_email(self):
        print("Test Email")
        self.assertEqual(self.employee1.email, "Corey.Schafer@test.email.org")
        self.assertEqual(self.employee2.email, "Sue.Smith@test.email.org")

        self.employee1.set_first_name = "John"
        self.employee2.set_first_name = "Jane"

        self.assertEqual(self.employee1.email, "John.Schafer@test.email.org")
        self.assertEqual(self.employee2.email, "Jane.Smith@test.email.org")

    def test_fullname(self):
        print("Test Fullname")
        self.assertEqual(self.employee1.fullname, "Corey Schafer")
        self.assertEqual(self.employee2.fullname, "Sue Smith")

        self.employee1.set_first_name = "John"
        self.employee2.set_first_name = "Jane"

        self.employee1.set_last_name = "Smith"
        self.employee2.set_last_name = "Stevens"

        self.assertEqual(self.employee1.fullname, "John Smith")
        self.assertEqual(self.employee2.fullname, "Jane Stevens")

    def test_apply_raise(self):
        print("Test Apply Raise")
        self.employee1.apply_raise()
        self.employee2.apply_raise()

        self.assertEqual(self.employee1.pay, 52500.525)
        self.assertEqual(self.employee2.pay, 63000.94500000001)

    def test_monthly_schedule(self):
        print("Test Monthly Schedule")

        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.employee1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.employee2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")
