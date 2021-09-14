from Base import Base

class AppointmentsPage(Base):
    appointment = '[data-testid="appointment"]'
    alert = '[data-testid="alert"]'
    pet_field = '[data-testid="pet"]'
    owner_field = '[data-testid="owner"]'
    date_field = '[data-testid="date"]'
    time_field = '[data-testid="time"]'
    symptoms_field = '[data-testid="symptoms"]'
    appointment_pet = 'p[1]/span'
    appointment_owner = 'p[2]/span'
    appointment_date = 'p[3]/span'
    appointment_time = 'p[4]/span'
    appointment_symptoms = 'p[5]/span'
    submit_button = '[data-testid="btn-submit"]'
    delete_button = '[data-testid="btn-delete"]'

    def add_appointment(self, pet, owner, date, time, symptoms):
        self.type(self.pet_field, pet)
        self.type(self.owner_field, owner)
        self.type(self.date_field, date)
        self.type(self.time_field, time)
        self.type(self.symptoms_field, symptoms)
        self.click(self.submit_button)

    def delete_appointment(self, index=0):
        self.click(self.delete_button, index)

    def check_if_appointment_exits(self, index=0):
        return self.check_existence_of(self.appointment, index)

    def check_appointment_pet(self, pet, index=0):
        return self.check_content_of(self.appointment, self.appointment_pet, pet, index)

    def check_appointment_owner(self, owner, index=0):
        return self.check_content_of(self.appointment, self.appointment_owner, owner, index)

    def check_appointment_date(self, date, index=0):
        return self.check_content_of(self.appointment, self.appointment_date, date, index)

    def check_appointment_time(self, time, index=0):
        return self.check_content_of(self.appointment, self.appointment_time, time, index)

    def check_appointment_symptoms(self, symptoms, index=0):
        return self.check_content_of(self.appointment, self.appointment_symptoms, symptoms, index)

    def check_alert_message(self, message):
        return self.check_text_of(self.alert, message)
