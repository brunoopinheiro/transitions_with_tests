import pytest  # NOQA
from src.client.typed_machine import TypedMachine, State


class TestTypedMachine:

    def setup_class(self):
        self.tm = TypedMachine()

    def test_typed_machine_initial_state(self):
        assert hasattr(self.tm.model, 'state')

    def test_typed_machine_function(self):
        self.tm.model.foo()
        assert self.tm.model.state == State.B
