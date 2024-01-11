def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for key, value in permanence_period:
            if key <= target_time <= value:
                counter = counter + 1

        return counter
    except (TypeError):
        return None
