def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours, minutes

def payment():
    entry_time_str = input("Enter the entry time (HH:MM): ")
    exit_time_str = input("Enter the exit time (HH:MM): ")

    entry_hours, entry_minutes = parse_time(entry_time_str)
    exit_hours, exit_minutes = parse_time(exit_time_str)

    total_minutes = (exit_hours - entry_hours) * 60 + (exit_minutes - entry_minutes)
    total_hrs = total_minutes // 60
    extra_min = total_minutes % 60
    print(f"total time you spend : {total_hrs}:{extra_min}")

    if extra_min <= 35 and extra_min>=25:
        extra_amt = 50
    elif extra_min>35:
        extra_amt = 100

    if total_hrs == 0:
        if extra_min <= 15:
            return 0
        else:
            return extra_amt
    elif total_hrs == 1:
        amount = 100 + extra_amt
    else:
        amount = 100 + 150 * (total_hrs - 1) + extra_amt

    if extra_min > 30:
        amount += 150

    return amount

print(payment())
