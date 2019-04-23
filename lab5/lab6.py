from itertools import combinations, permutations

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
names = ["Elena", "Anna", "Boris", "Semen", "Dmitry"]

def generate_schedule():
    names_combinations = list(combinations(names, 2))
    possible_combinations = list(permutations(names_combinations, 5))
    for combination in possible_combinations:
        hyp_schedule = dict(zip(days, combination))
        yield hyp_schedule


def test_schedule(schedule):
    def check_Anna_Boris_pair(pair):
        if ("Anna" in pair and "Boris" in pair):
            return True
        return False

    def check_Semen_Elena_pair(pair):
        if not (("Semen" in pair) and ("Elena" in pair)):
            return True

    #check if Anna and Boris work together and Semen and Elena don't work together
    for day, pair in schedule.items():
        if not check_Semen_Elena_pair(pair):
            return False

    for day, pair in schedule.items():
        if check_Anna_Boris_pair(pair):
            break
        elif day == "Friday":
            return False

    #check if anyone works on Thursday and Friday
    if (schedule["Thursday"][0] in schedule["Friday"]) or (
            schedule["Thursday"][1] in schedule["Friday"]):
        return False

    #check if Boris works on Thursday
    if "Boris" not in schedule["Thursday"]:
        return False

    #check if Elena doesn't  work on Friday
    if "Elena" in schedule["Friday"]:
        return False

    #check if Boris, Dmitry or Elena work everyday
    for day, pair in schedule.items():
        if not (("Elena" in pair) or ("Boris" in pair) or ("Dmitry" in pair)):
            return False
    #check if Dmitry works on Monday
    if "Dmitry" not in schedule["Monday"]:
        return False

    #check if one of those who work on Wednesday works with Dmitry on another day
    dmitry_days = []
    for day, pair in schedule.items():
        if "Dmitry" in pair and day != "Wednesday":
            dmitry_days.append(pair)

    checks = []
    for dmitry_day in dmitry_days:
        checks.append(schedule["Wednesday"][0] in dmitry_day
                      or schedule["Wednesday"][1] in dmitry_day)
    if not any(checks):
        return False

    #check if one works on Mondays and Tuesdays
    checks = []
    for name in names:
        if name in schedule["Monday"] and name in schedule["Tuesday"]:
            checks.append(True)
    if not any(checks):
        return False

    #check if any pair works twice
    for day1, pair1 in schedule.items():
        for day2, pair2 in schedule.items():
            if day1 != day2 and pair1 == pair2:
                return False

    #check if anyone works more than two
    checks = {}
    for name in names:
        checks[name] = 0

    for name in names:
        for day, pair in schedule.items():
            if name in pair:
                checks[name] += 1

    for name, num in checks.items():
        if num > 2:
            return False

    return True


if __name__ == "__main__":
    results = []
    iteration = 0
    for schedule in generate_schedule():
        iteration+=1
        if test_schedule(schedule):
            print("------------------------Solution--------------------------")
            for day, pair in schedule.items():
                print("{}  - {} and {}".format(day, pair[0], pair[1]))
            break
    
