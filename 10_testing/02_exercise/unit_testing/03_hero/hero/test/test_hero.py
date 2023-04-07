from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("HERO", 1, 11.11, 11.11, )
        self.enemy = Hero("ENEMY", 1, 11.11, 11.11, )

    def test_correct_initialisation(self):
        self.assertEqual("HERO", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(11.11, self.hero.health)
        self.assertEqual(11.11, self.hero.damage)

    def test_battle_method_with_same_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_rase_value_error_if_hero_no_health_left(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as vale:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(vale.exception))

    def test_battle_method_rase_value_error_if_enemy_no_health_left(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as vale:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(vale.exception))

    def test_battle_method_return_draw_scenario_as_it_will_with_given_values_it_test_setUp(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_return_you_win(self):
        self.hero.health += self.enemy.health
        self.hero.damage += self.enemy.health

        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)  # must be added +1 to lvl as bonus
        self.assertEqual(16.11, self.hero.health)  # hero + enemy - enemy_dmg*lvl + bonus (11.11+11.11-11.11*1 +5)
        self.assertEqual(27.22, self.hero.damage)  # hero + enemy + bonus ( 11.11 + 11.11 + 5)
        self.assertEqual("You win", result)

    def test_battle_return_you_lose(self):
        self.enemy.health += self.hero.health
        self.enemy.damage += self.hero.damage

        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)  # same as above
        self.assertEqual(16.11, self.enemy.health)
        self.assertEqual(27.22, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test___str__method_return_correct_message(self):
        self.assertEqual("Hero HERO: 1 lvl\nHealth: 11.11\nDamage: 11.11\n", str(self.hero))


if __name__ == '__main__':
    main()
