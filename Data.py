FEDERAL_TAX = 0.153
CO_STATE_TAX = 0.0455
FICA_STATE_INS_TAX = 0.0765


class Data:

    def __init__(self):
        self.wage: int = 0
        self.days: int = 0
        self.total_hours: int = 0
        self.total_tips: int = 0
        self.today_hours: int = 0
        self.today_tips: int = 0
        self.total_wages_earned: int = 0

    def add_hours(self, hours: int):
        self.total_hours += hours
        self.days += 1

    def add_to_total_wages_earned(self):
        self.total_wages_earned += self.wage * self.today_hours

    def get_today_earned_no_tips(self):
        return self.wage * self.today_hours

    def get_today_earned_with_tips(self):
        return self.wage * self.today_hours + self.today_tips

    def get_average_hours(self):
        if self.days != 0:
            return self.total_hours / self.days
        else:
            return 0

    def get_average_tips(self):
        if self.days != 0:
            return self.total_tips / self.days
        else:
            return 0

    def get_today_average_wage_with_tips(self):
        if self.total_hours != 0:
            return self.wage + (self.today_tips / self.today_hours)
        else:
            return 0

    def get_overall_average_wage_no_tips(self):
        if self.total_hours != 0:
            return self.total_wages_earned / self.total_hours
        else:
            return 0

    def get_overall_average_wage_with_tips(self):
        if self.total_hours != 0:
            return (self.total_wages_earned / self.total_hours) + (self.total_tips / self.total_hours)
        else:
            return 0

    def get_overall_average_wage_post_tax(self):
        return self.get_overall_average_wage_no_tips() - (self.get_overall_average_wage_no_tips() * FEDERAL_TAX) - (
                self.get_overall_average_wage_no_tips() * CO_STATE_TAX) - (
                       self.get_overall_average_wage_no_tips() * FICA_STATE_INS_TAX)

    def get_today_earned_post_tax(self):
        return self.get_today_earned_no_tips() - (self.get_today_earned_no_tips() * FEDERAL_TAX) - (
                self.get_today_earned_no_tips() * CO_STATE_TAX) - (
                       self.get_today_earned_no_tips() * FICA_STATE_INS_TAX)
