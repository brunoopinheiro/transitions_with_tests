import pytest  # NOQA
from src.client.predefined_model import TypedMachine


class TestPredefinedModel:

    def setup_class(self):
        self.state_machine = TypedMachine()

    def setup_method(self):
        self.state_machine.machine.set_state('A')

    def test_state_execution(self):
        assert self.state_machine.model.state == 'A'

    def test_trigger_changes_state(self):
        self.state_machine.model.trigger('go')
        assert self.state_machine.model.state == 'B'

    def test_triggering_defined_state(self):
        self.state_machine.model.go()
        assert self.state_machine.model.state == 'B'
