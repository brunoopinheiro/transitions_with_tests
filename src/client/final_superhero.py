# code adapted from https://github.com/pytransitions/transitions
from transitions import Machine, State


class FinalSuperhero:

    states = [
        State(name='idling'),
        State(name='rescuing_kitten'),
        State(name='offender_gone', final=True),
        State(name='offender_caught', final=True),
    ]

    transitions = [
        {
            'source': 'idling',
            'trigger': 'called',
            'dest': 'rescuing_kitten',
        },
        {
            'source': 'rescuing_kitten',
            'trigger': 'intervene',
            'dest': 'offender_gone',
            'conditions': 'offender_is_faster',
        },
        {
            'source': 'rescuing_kitten',
            'trigger': 'intervene',
            'dest': 'offender_caught',
        },
    ]

    @property
    def speed(self) -> int:
        return self.__speed

    def __init__(self, speed: int) -> None:
        self.machine = Machine(
            model=self,
            states=FinalSuperhero.states,
            transitions=FinalSuperhero.transitions,
            initial='idling',
            on_final='claim_success',
        )
        self.__speed = speed

    def offender_is_faster(self, offender_speed: int) -> bool:
        return self.speed < offender_speed

    def claim_success(self, **kwargs):
        print('The Kitten is safe!')
