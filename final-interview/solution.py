def turtle_outruns_cheetah(vegetarian_food_in_finish_line, zebra_is_alive, race_track_lenght_meters, zebra_start_position_racetrack):
    if not zebra_is_alive:
        if zebra_start_position_racetrack < race_track_lenght_meters:
            if vegetarian_food_in_finish_line:
                return True
            return False
    else:
        if zebra_start_position_racetrack > race_track_lenght_meters/2:
            return False
        else:
            if vegetarian_food_in_finish_line:
                return True
            return False