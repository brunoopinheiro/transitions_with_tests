import pytest  # NOQA
from src.client.typed_model import TypedMachine, simple_config


class TestTypedMachine:

    def setup_class(self):
        self.tm = TypedMachine()
        self.config_dict = simple_config

    def setup_method(self):
        initial_state = self.config_dict.get('initial')
        self.tm.machine.set_state(initial_state)

    def test_typed_machine_state(self):
        initial_state = self.config_dict.get('initial')
        assert self.tm.model.state == initial_state

    def test_typed_machine_trigger(self):
        self.tm.model.go()
        assert self.tm.model.state == 'B'
