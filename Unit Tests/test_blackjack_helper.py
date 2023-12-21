from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 9), "Drew a 9\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([5], draw_card), 5)
    self.assertEqual(mock_random([8], draw_card), 8)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "Your"), '-----------\nYour\n-----------\n')
    self.assertEqual(get_print(print_header, ""), '-----------\n\n-----------\n')
    self.assertEqual(get_print(print_header, "YOUR TURN"), '-----------\nYOUR TURN\n-----------\n')
    self.assertEqual(get_print(print_header, "1.5"), '-----------\n1.5\n-----------\n')

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)
    self.assertEqual(mock_random([1, 1], draw_starting_hand, "USER"), 22)
    self.assertEqual(mock_random([11, 12], draw_starting_hand, "IRON MAN"), 20)
    self.assertEqual(mock_random([13, 1], draw_starting_hand, "HULK"), 21)
    self.assertEqual(mock_random([12, 5], draw_starting_hand, "LOKI"), 15)
    self.assertEqual(mock_random([1, 5], draw_starting_hand, "THANOS"), 16)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), 'Final hand: 21.\nBLACKJACK!\n')
    self.assertEqual(get_print(print_end_turn_status, 25), 'Final hand: 25.\nBUST.\n')
    self.assertEqual(get_print(print_end_turn_status, 18), 'Final hand: 18.\n')
    self.assertEqual(get_print(print_end_turn_status, 10), 'Final hand: 10.\n')

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 18, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 18), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 17, 17), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 19, 18), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 18, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 23, 23), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 23, 19), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 5, 23), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    
if __name__ == '__main__':
    unittest.main()
