import pytest  # NOQA
from src.client.matter import StatefulLump


class TestStatefulLump:

    skipif_condition = True

    def setup_class(self):
        self.stateful_lump = StatefulLump()

    def setup_method(self):
        self.stateful_lump.initiate()
        print(f'\nInitiated: {self.stateful_lump.initiated}')

    def teardown_method(self):
        self.stateful_lump.end_operation()
        print(f'\nInitiated: {self.stateful_lump.initiated}')

    def test_machine_creation(self):
        assert hasattr(self.stateful_lump, 'lump')
        assert hasattr(self.stateful_lump, 'machine')
        assert hasattr(self.stateful_lump.lump, 'state')

    def test_lump_state_starts_at_solid(self):
        assert self.stateful_lump.lump.state == 'solid'

    @pytest.mark.parametrize(
        'source, trigger, dest',
        [
            ('solid', 'melt', 'liquid'),
            ('liquid', 'evaporate', 'gas'),
            ('gas', 'ionize', 'plasma'),
            ('solid', 'sublimate', 'gas'),
        ]
    )
    def test_state_transition_via_method(self, source, trigger, dest):
        setattr(self.stateful_lump.lump, 'state', source)
        callable_function = getattr(self.stateful_lump.lump, trigger)
        callable_function()
        assert self.stateful_lump.lump.state == dest

    @pytest.mark.parametrize(
        'source, trigger, dest',
        [
            ('solid', 'melt', 'liquid'),
            ('liquid', 'evaporate', 'gas'),
            ('gas', 'ionize', 'plasma'),
            ('solid', 'sublimate', 'gas'),
        ]
    )
    def test_state_transition_via_trigger_method(self, source, trigger, dest):
        setattr(self.stateful_lump.lump, 'state', source)
        self.stateful_lump.lump.trigger(trigger)
        assert self.stateful_lump.lump.state == dest

    @pytest.mark.skip(reason='Demonstration')
    def test_skipping_mark(self):
        assert self.stateful_lump.initiated is True

    @pytest.mark.skipif(skipif_condition is True, reason='Demonstration if')
    def test_skipping_skipif_mark(self):
        assert self.stateful_lump.initiated is True

    def test_report_state(self, capsys):
        self.stateful_lump.report_state()
        captured = capsys.readouterr()
        expected = f'State: {self.stateful_lump.lump.state}\n'
        assert captured.out == expected
