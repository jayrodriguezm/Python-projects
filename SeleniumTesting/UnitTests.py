import unittest
from Appointments_Page import AppointmentsPage
from time import sleep


class UnitTests(unittest.TestCase):
    page = None
    website = "http://localhost:3000"
    empty_field = ""
    test_pet_1 = "Choco"
    test_pet_2 = "Mia"
    test_pet_3 = "Yeiborsh"
    test_owner = "Jairo"
    test_date = "10-09-2021"
    test_past_date = "10-09-2020"
    test_incomplete_date = "10-09"
    test_time = "6:00PM"
    test_incomplete_time = "6:00"
    test_symptoms = "Cat only sleeps"
    one_very_log_word = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

    @classmethod
    def setUp(self):
        self.page = AppointmentsPage(self.website)

    def test_valid_values(self):
        self.page.add_appointment(self.test_pet_1, self.test_owner, self.test_date, self.test_time, self.test_symptoms)
        self.assertTrue(self.page.check_if_appointment_exits(), "Appointment does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_1), "Pet mismatch")
        self.assertTrue(self.page.check_appointment_owner(self.test_owner), "Owner mismatch")
        self.assertTrue(self.page.check_appointment_date("2021-10-09"), "Date mismatch")
        self.assertTrue(self.page.check_appointment_time("18:00"), "Time mismatch")
        self.assertTrue(self.page.check_appointment_symptoms(self.test_symptoms), "Symptoms mismatch")

    def test_invalid_pet(self):
        self.page.add_appointment(self.empty_field, self.test_owner, self.test_date, self.test_time, self.test_symptoms)
        self.assertFalse(self.page.check_if_appointment_exits(), "Appointment should not exist")
        self.assertTrue(self.page.check_alert_message("All fields are required"), "Alert message is incorrect")

    def test_long_word(self):
        self.page.add_appointment(self.one_very_log_word, self.test_owner, self.test_date, self.test_time,
                                  self.test_symptoms)
        self.assertTrue(self.page.check_if_appointment_exits(), "Appointment does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.one_very_log_word), "Pet mismatch")

    def test_invalid_owner(self):
        self.page.add_appointment(self.test_pet_1, self.empty_field, self.test_date, self.test_time, self.test_symptoms)
        self.assertFalse(self.page.check_if_appointment_exits(), "Appointment should not exist")
        self.assertTrue(self.page.check_alert_message("All fields are required"), "Alert message is incorrect")

    def test_date_in_past(self):
        self.page.add_appointment(self.test_pet_1, self.test_owner, self.test_past_date, self.test_time,
                                  self.test_symptoms)
        self.assertFalse(self.page.check_if_appointment_exits(), "Appointment should not exist")
        self.assertTrue(self.page.check_alert_message("All fields are required"), "Alert message is incorrect")

    def test_multiple_appointments(self):
        self.page.add_appointment(self.test_pet_1, self.test_owner, self.test_date, self.test_time, self.test_symptoms)
        sleep(1)
        self.page.add_appointment(self.test_pet_2, self.test_owner, self.test_date, self.test_time, self.test_symptoms)
        sleep(1)
        self.assertTrue(self.page.check_if_appointment_exits(0), "Appointment 1 does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_1, 0), "Pet 1 mismatch")
        self.assertTrue(self.page.check_if_appointment_exits(1), "Appointment 2 does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_2, 1), "Pet 2 mismatch")
        self.page.add_appointment(self.test_pet_3, self.test_owner, self.test_date, self.test_time, self.test_symptoms)
        sleep(1)
        self.assertTrue(self.page.check_if_appointment_exits(2), "Appointment 3 does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_3, 2), "Pet 3 mismatch")
        self.page.delete_appointment(0)
        self.assertTrue(self.page.check_if_appointment_exits(0), "Appointment 1 does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_2, 0), "Pet 2 mismatch")
        self.assertTrue(self.page.check_if_appointment_exits(1), "Appointment 2 does not exist")
        self.assertTrue(self.page.check_appointment_pet(self.test_pet_3, 1), "Pet 3 mismatch")

    @classmethod
    def tearDown(self):
        self.page.close_driver()

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(FullStackLabs)
        unittest.TextTestRunner(verbosity=2).run(suite)
