import pytest
from src.client.super_matter import SuperStatefulLump


class TestSuperStatefulLump:

    def setup_class(self):
        self.super_lump = SuperStatefulLump()

    def test_machine_creation(self):
        assert hasattr(self.super_lump, 'lump')
        assert hasattr(self.super_lump, 'machine')
        assert hasattr(self.super_lump.lump, 'state')

    def test_lump_starts_at_solid(self):
        assert self.super_lump.lump.state == 'solid'

    @pytest.mark.parametrize(
        'source, trigger, dest',
        [
            ('solid', 'melt', 'liquid'),
            ('liquid', 'evaporate', 'gas'),
            ('solid', 'sublimate', 'gas'),
            ('gas', 'ionize', 'plasma'),
        ]
    )
    def test_callback_execution_at_transition(
        self,
        capsys,
        source,
        trigger,
        dest,
    ):
        say_hello_text = 'Hello, new state!\n'
        setattr(self.super_lump.lump, 'state', source)
        self.super_lump.lump.trigger(trigger)
        captured = capsys.readouterr()
        assert captured.out == say_hello_text
        assert self.super_lump.lump.state == dest
