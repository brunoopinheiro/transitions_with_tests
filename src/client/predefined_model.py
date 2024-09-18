# code adapted from https://github.com/pytransitions/transitions
from transitions import Machine


class PredefinedModel:

    # this will be used to keep track of the model's state
    state: str

    def go(self) -> bool:
        raise RuntimeError('Should be overriden by the Machine')

    def trigger(self, trigger_name: str) -> bool:
        raise RuntimeError('Should be overriden by the Machine')


class TypedMachine:

    def __init__(self) -> None:
        self.model = PredefinedModel()
        self.machine = Machine(
            model=self.model,
            states=['A', 'B'],
            transitions=[['go', 'A', 'B']],
            initial='A',
            model_override=True,
        )
