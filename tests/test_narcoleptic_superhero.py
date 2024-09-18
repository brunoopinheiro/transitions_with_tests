import pytest
from unittest.mock import patch
from src.client.narcoleptic_superhero import NarcolepticSuperhero
from transitions import MachineError


@pytest.fixture
def batman() -> NarcolepticSuperhero:
    return NarcolepticSuperhero('Batman')


def test_narcoleptic_superhero_initial_state(batman):
    assert batman.state == 'asleep'


def test_wakeup_changes_state(batman):
    batman.wake_up()
    assert batman.state == 'hanging out'


def test_nap_changes_state(batman):
    batman.nap()
    assert batman.state == 'asleep'


def test_raise_machine_error_from_asleep(batman):
    assert batman.state == 'asleep'
    with pytest.raises(MachineError):
        batman.clean_up()


def test_multiple_transitions(batman):
    batman.wake_up()
    batman.work_out()
    assert batman.state == 'hungry'
    assert batman.kittens_rescued == 0


def test_distress_call(batman, capsys):
    batman.distress_call()
    captured = capsys.readouterr()
    assert captured.out == 'Beauty, eh?\n'
    assert batman.state == 'saving the world'


def test_complete_mission_updates_kittens_rescued(batman):
    batman.distress_call()
    batman.complete_mission()
    assert batman.state == 'sweaty'
    assert batman.kittens_rescued == 1


def test_goes_to_sleep_if_cleanup_while_is_exhausted(batman):
    with patch(
        'src.client.narcoleptic_superhero.NarcolepticSuperhero.is_exhausted',
        return_value=True,
    ):
        batman.distress_call()
        batman.complete_mission()
        batman.clean_up()
        assert batman.state == 'asleep'


def test_hanging_out_after_cleanup_while_not_exhausted(batman):
    with patch(
        'src.client.narcoleptic_superhero.NarcolepticSuperhero.is_exhausted',
        return_value=False,
    ):
        batman.distress_call()
        batman.complete_mission()
        batman.clean_up()
        assert batman.state == 'hanging out'
