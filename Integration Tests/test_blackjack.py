from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand more than 21.
        The dealer wins as both of them busts.
        '''
        output = run_test([10, 9, 4], ['c', 'y'], [4, 10, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? c\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 10\n" \
                   "Dealer has 14.\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_blackjack(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand of 21.
        The result is push both of them have same hand value.
        '''
        output = run_test([6, 5, 12], ['y'], [10, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_17(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand of 17.
        The result is push as both of them have same hand value.
        '''
        output = run_test([7, 12], ['n'], [8, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a Queen\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_busts_user_stands(self, input_mock, randint_mock):
        '''
        The dealer ends up with a hand more than 21 but the user has less or equal to than 21 (5 in this test).
        The user wins by not busting.
        '''
        output = run_test([2,3], ['n'], [1, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? n\n" \
                   "Final hand: 5.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_busts_dealer_stands(self, input_mock, randint_mock):
        '''
        The user gets the hand greater than 21 and dealer has less than or equal to 21 (18 in this test).
        The dealer wins by not busting..
        '''
        output = run_test([2, 3, 5, 8, 1], ['y', 'y','y'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 29.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_stand_user_win(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([10, 5, 3], ['y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_backjack_user_non_blackjack(self, input_mock, randint_mock):
        '''
        The dealer end up with a hand 21 and user receive cards that end up with a hand other than 21 (16 in this case).
        The dealer wins by having a BLACKJACK.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [1, 5, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_backjack_dealer_non_blackjack(self, input_mock, randint_mock):
        '''
        The user end up with a hand 21 and dealer receive cards that end up with a hand other than 21 (20 in this case).
        The user wins by having a BLACKJACK.
        '''
        output = run_test([1, 11], [], [1, 5, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Jack\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjack_dealer_bust(self, input_mock, randint_mock):
        '''
        The user end up with a hand of 21 and dealer with more than 21.
        The user wins by having a BlackJack.
        '''
        output = run_test([2, 3, 5, 2, 9], ['y', 'y', 'y'], [3, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 3\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_backjack_user_bust(self, input_mock, randint_mock):
        '''
        The dealer end up with a hand 21 and user receive cards that end up with more than 21.
        The dealer wins by having a BLACKJACK.
        '''
        output = run_test([3, 9, 1], ['y'], [1, 5, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def both_bust_user_higher_hand(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand more than 21. user hand higher than dealer's. 
        The dealer wins as both of them busts.
        '''
        output = run_test([10, 10, 4], ['y'], [4, 10, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 10\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 10\n" \
                   "Dealer has 14.\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def both_bust_dealer_higher_hand(self, input_mock, randint_mock): 
        '''
        Both the dealer and user receive cards that end up with a hand more than 21. Dealer hand higher than user's. 
        The dealer wins as both of them busts.
        '''
        output = run_test([10, 9, 4], ['y'], [4, 10, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 10\n" \
                   "Dealer has 14.\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
