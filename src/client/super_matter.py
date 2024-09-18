# Code adapted from https://github.com/pytransitions/transitions
from transitions import Machine, State
from typing import List, Tuple


class SuperMatter:

    def say_hello(self):
        print('Hello, new state!')

    def say_goodbye(self):
        print('Goodbye, old state!')


class SuperStatefulLump:

    def __define_states(self) -> List[State]:
        callback_signature = 'say_hello'
        solid = State(name='solid', on_enter=[callback_signature])
        liquid = State(name='liquid', on_enter=[callback_signature])
        gas = State(name='gas', on_enter=[callback_signature])
        plasma = State(name='plasma', on_enter=[callback_signature])
        return [solid, liquid, gas, plasma]

    def __define_transitions(self) -> List[Tuple[str, str, str]]:
        transitions_list = [
            ('solid', 'melt', 'liquid'),
            ('liquid', 'evaporate', 'gas'),
            ('solid', 'sublimate', 'gas'),
            ('gas', 'ionize', 'plasma'),
        ]
        return transitions_list

    def __init__(self) -> None:
        self.lump = SuperMatter()
        states = self.__define_states()
        self.machine = Machine(
            model=self.lump,
            states=states,
            initial='solid',
        )
        transitions_list = self.__define_transitions()
        for source, trigger, dest in transitions_list:
            self.machine.add_transition(trigger, source, dest)
