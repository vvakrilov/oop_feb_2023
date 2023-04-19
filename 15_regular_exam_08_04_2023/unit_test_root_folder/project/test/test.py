from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    _name = 'Player'
    _age = 20
    _points = 22.22
    _no_wins = []
    _place = 'ArenaArmeec'
    _got_wins = ['ArenaArmeec, Sydney SuperDome']
    _other = 'Other'

    def setUp(self):
        self.tennis_player = TennisPlayer(self._name, self._age, self._points)
        self.other_player = TennisPlayer(self._other, self._age, self._points)

    def test_correct_initialization(self):
        self.assertEqual(self._name, self.tennis_player.name)
        self.assertEqual(self._age, self.tennis_player.age)
        self.assertEqual(self._points, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_rise_value_error_with_less_than_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer('T', self._age, self._points)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter_rise_value_error_with_less_than_18_years_old_player(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer(self._name, 10, self._points)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_appends_new_win_to_list(self):
        self.tennis_player.add_new_win('ArenaArmeec')
        self.assertEqual(['ArenaArmeec', ], self.tennis_player.wins)

    def test_add_new_win_returns_tournament_has_been_already_won(self):
        self.tennis_player.wins.append(self._place)
        result = self.tennis_player.add_new_win('ArenaArmeec')
        self.assertEqual("ArenaArmeec has been already added to the list of wins!", result)

    def test_str_repr_return_correct_message(self):
        self.tennis_player.wins = self._got_wins
        self.assertEqual(
            f"Tennis Player: {self._name}\n"
            f"Age: {self._age}\n"
            f"Points: {self._points:.1f}\n"
            f"Tournaments won: {', '.join(self._got_wins)}",
            str(self.tennis_player)
        )

    def test_less_than_method_returns_message_that_other_player_is_top_speed_player(self):
        self.tennis_player.points -= self.tennis_player.points
        result = self.tennis_player < self.other_player
        self.assertEqual(f'{self._other} is a top seeded player and he/she is better than {self._name}', result)

    def test_less_than_method_returns_that_self_player_is_better_player_than_other_one(self):
        self.tennis_player.points += self.other_player.points
        result = self.tennis_player < self.other_player
        self.assertEqual(f'{self._name} is a better player than {self._other}', result)


if __name__ == '__main__':
    main()
