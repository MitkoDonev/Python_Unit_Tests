import requests


class Employee:
    raise_value = 1.05

    def __init__(self, first_name, last_name, pay):
        self.__first_name = first_name.lower()
        self.__last_name = last_name.lower()
        self.__pay = pay

    @property
    def first_name(self):
        return self.__first_name.capitalize()

    @first_name.setter
    def set_first_name(self, new_name):
        self.__first_name = new_name.lower()

    @property
    def last_name(self):
        return self.__last_name.capitalize()

    @last_name.setter
    def set_last_name(self, new_name):
        self.__last_name = new_name.lower()

    @property
    def pay(self):
        return self.__pay

    @pay.setter
    def set_pay(self, new_pay):
        self.__pay = new_pay

    @property
    def email(self):
        return f"{self.__first_name.capitalize()}.{self.last_name.capitalize()}@test.email.org"

    @property
    def fullname(self):
        return f"{self.__first_name.capitalize()} {self.last_name.capitalize()}"

    def apply_raise(self):
        self.__pay = float(self.pay * self.raise_value)

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last_name}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
