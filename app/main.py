from engine import setup, constants, utils
from engine.routine import Routine, DefaultRoutine
from model import model


def main():
    setup.run()
    events = {
        "workout": "1 hour workout",
        "shower": "take a cold shower",
        "breakfast": "make "
    }

    default_routine = DefaultRoutine(utils.Time(10,30), constants.playlists, )
    
    # awake_sad_routine = Routine("awake-sad", default_routine)
    # awake_neutral_routine = Routine("awake-neutral", default_routine)
    # awake_happy_routine = Routine("awake-happy", default_routine)
    # tired_sad_routine = Routine("tired-sad", default_routine)
    # tired_neutral_routine = Routine("tired-neutral", default_routine)
    # tired_happy_routine = Routine("tired-happy", default_routine)

    # generate routines
    routines = {label: Routine(label, default_routine) for label in constants.labels}

    # get img
    img = utils.get_picture()    

    # get label from model
    l = constants.labels[model.run(img)]




if __name__ == "__main__":
    main()