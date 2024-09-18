import pytest  # NOQA
from src.client.final_superhero import FinalSuperhero


class TestFinalSuperhero:

    def test_hero_saving_kitten(self, capsys):
        self.hero = FinalSuperhero(speed=10)
        self.hero.called()
        assert self.hero.is_rescuing_kitten() is True

        self.hero.intervene(offender_speed=5)
        assert self.hero.is_offender_caught() is True
        captured = capsys.readouterr()
        assert captured.out == 'The Kitten is safe!\n'

    def test_hero_failing(self, capsys):
        self.hero = FinalSuperhero(speed=10)
        self.hero.called()
        assert self.hero.is_rescuing_kitten() is True

        self.hero.intervene(offender_speed=15)
        assert self.hero.machine.get_state(self.hero.state).final
        assert self.hero.is_offender_gone()
