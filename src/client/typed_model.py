from src.generator.typed_machine_generator import simple_config
from src.generator.generated_model import BaseModel
from random import random
from transitions import Machine


class Model(BaseModel):

    def call_this(self) -> bool:
        return random() > 0.5


class TypedMachine:

    def __init__(self) -> None:
        self.model = Model()
        self.machine = Machine(
            self.model,
            **simple_config,
        )
