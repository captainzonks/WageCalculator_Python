from pathlib import Path

from Data import Data


def ask_for_wage(data: Data):
    while True:
        user_input = input("Please enter your wage: ")
        try:
            wage = float(user_input)
            if isinstance(wage, float):
                break
        except ValueError:
            print("Value is not a number.")
            pass

    data.wage = float(wage)


def ask_to_change_wage(data: Data):
    answer = input(f"Would you like to change your wage from ${data.wage:.2f}? ('y' or 'n') ")
    if answer.lower() == 'y':
        ask_for_wage(data)


def ask_for_hours(data: Data):
    while True:
        user_input = input("How many hours did you work today? ")
        try:
            hours = float(user_input)
            if isinstance(hours, float):
                break
        except ValueError:
            print("Value is not a number.")
            pass

    data.today_hours = float(hours)
    data.add_hours(float(hours))


def ask_for_tips(data: Data):
    while True:
        user_input = input("Enter tips: ")
        try:
            tips = float(user_input)
            if isinstance(tips, float):
                break
        except ValueError:
            print("Value is not a number.")
            pass

    data.today_tips = float(tips)
    data.total_tips += float(tips)


def print_pretty_data(data: Data):
    print(f"Wage: ${data.wage:.2f} / hr")
    print(f"Total hours worked: {data.total_hours} hrs")
    print(f"Earned today (tips, no tax): ${data.get_today_earned_with_tips():.2f}")
    print(f"Earned today (w/o tips, taxed): ${data.get_today_earned_post_tax():.2f}")
    print(f"Total all-time tips: ${data.total_tips:.2f}")
    print(f"Tips Average: ${data.get_average_tips():.2f}")
    print(f"Today's Adjusted Hourly Rate (tips, no tax): ${data.get_today_average_wage_with_tips():.2f}")
    print(f"Overall Adjusted Hourly Rate (tips, no tax): ${data.get_overall_average_wage_with_tips():.2f}")
    print(f"Overall Adjusted Hourly Rate (w/o tips, taxed): ${data.get_overall_average_wage_post_tax():.2f}")


if __name__ == '__main__':
    today_data = Data()
    exists = False

    my_file = Path("data")
    if my_file.is_file():
        exists = True
    else:
        ask_for_wage(today_data)

    if exists:
        with open("data", 'r') as file:
            today_data.wage = float(file.readline())
            today_data.total_hours = float(file.readline())
            today_data.days = int(file.readline())
            today_data.total_tips = float(file.readline())
            today_data.today_hours = float(file.readline())
            today_data.today_tips = float(file.readline())
            today_data.total_wages_earned = float(file.readline())

    ask_to_change_wage(today_data)
    ask_for_hours(today_data)
    ask_for_tips(today_data)
    today_data.add_to_total_wages_earned()
    print_pretty_data(today_data)

    with open("data", 'w') as file:
        file.write(f"{today_data.wage}\n")
        file.write(f"{today_data.total_hours}\n")
        file.write(f"{today_data.days}\n")
        file.write(f"{today_data.total_tips}\n")
        file.write(f"{today_data.today_hours}\n")
        file.write(f"{today_data.today_tips}\n")
        file.write(f"{today_data.total_wages_earned}\n")
