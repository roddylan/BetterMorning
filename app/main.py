from engine import setup, constants, utils
from engine.routine import Routine, DefaultRoutine
from model import model
import numpy as np


def main():
    setup.run()
    events = {
        "workout": "1 hour workout",
        "rinse": "take a cold rinse",
        "shower": "take a cold shower",
        "breakfast": "make breakfast according to meal plan"
    }

    sched = utils.Schedule(events)
    sched.make_schedule("tired-sad", ["rinse", "breakfast", "workout", "shower"])
    sched.make_schedule("awake-sad", ["breakfast", "workout", "shower"])
    sched.make_schedule("tired-happy", ["rinse", "workout", "shower",  "breakfast"])
    sched.make_schedule("awake-happy", ["workout", "shower",  "breakfast"])
    sched.make_schedule("tired-neutral", ["rinse", "workout", "shower",  "breakfast"])
    sched.make_schedule("awake-neutral", ["workout", "shower",  "breakfast"])

    
    default_routine = DefaultRoutine(bedtime=utils.Time(10,30), spotify=constants.playlists, schedule=sched, 
                                     bus_schedule=[utils.Time(8,20), utils.Time(8,50)], )
    
    # awake_sad_routine = Routine("awake-sad", default_routine)
    # awake_neutral_routine = Routine("awake-neutral", default_routine)
    # awake_happy_routine = Routine("awake-happy", default_routine)
    # tired_sad_routine = Routine("tired-sad", default_routine)
    # tired_neutral_routine = Routine("tired-neutral", default_routine)
    # tired_happy_routine = Routine("tired-happy", default_routine)

    # generate routines
    routines = {label: Routine(label, default_routine) for label in constants.labels}

    # get img
    img = utils.get_picture() # TODO: get pic from phone
    if not img:
        i = np.randint(0, len(constants.labels))
        l = constants.labels[i]
    else:
        # get label from model
        l = constants.labels[model.run(img)]

    routines[l].run()




if __name__ == "__main__":
    main()