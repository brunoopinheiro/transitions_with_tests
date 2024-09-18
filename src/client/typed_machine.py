from enum import Enum
from transitions.experimental.utils import (
    with_model_definitions,
    event,
    add_transitions,
    transition
)
from transitions import Machine


class State(Enum):
    A = 'A'
    B = 'B'
    C = 'C'


class Model:

    state: State = State.A

    @add_transitions(
        transition(source=State.A, dest=State.B),
        [State.C, State.A],
    )
    @add_transitions(transition(source=State.B, dest=State.A))
    def foo(self):
        ...

    bar = event(
        {'source': State.B, 'dest': State.A, 'conditions': lambda: False},
        transition(source=State.B, dest=State.C),
    )


@with_model_definitions
class MyMachine(Machine):
    pass


class TypedMachine:

    def __init__(self) -> None:
        self.model = Model()
        self.machine = MyMachine(
            self.model,
            states=State,
            initial=Model.state,
        )
