"""
Dmitry likes TopCoder Single Round Matches. Once, he registered for an SRM and was waiting for the coding phase to begin. To entertain himself while waiting, he decided to play the following game.

He makes a pile of cards, and on each card, he writes the number of an SRM in which he has competed. No two cards contain the same number. He then takes turns until the pile is empty. Each turn consists of the following sequence of actions:

*Dmitry chooses an arbitrary card from the pile. Let A be the number written on this card.
*The card with number A is removed from the pile.
*If the pile contains a card with number A-1, that card is removed from the pile.
*If the pile contains a card with number A+1, that card is removed from the pile.

The game is finished when the pile becomes empty. It's fun to play the game, so Dmitry wants to spend as much time as possible playing it.

You are given a int[] cards containing the numbers written on the cards in the pile before the start of the game. Return the largest possible number of turns in which Dmitry can finish the game.

Definition:
Class:  SRMCards
Method: maxTurns
Parameters: int[]
Returns:  int
Method signature: int maxTurns(int[] cards)
(be sure your method is public)


Constraints
- cards will contain between 1 and 50 elements, inclusive.
- Each element of cards will be between 1 and 499, inclusive.
- All elements of cards will be distinct.

Examples
0)

{498, 499}
Returns: 1
In the first turn, Dmitry can choose A = 498 or A = 499. In any of these cases both cards will be removed from the pile and the game will be finished.
1)

{491, 492, 495, 497, 498, 499}
Returns: 4
One out of many possible ways to spend 4 turns playing this game is to choose the following numbers in each turn: 497, 499, 495, 492.
2)

{100, 200, 300, 400}
Returns: 4
3)

{11, 12, 102, 13, 100, 101, 99, 9, 8, 1}
Returns: 6
Note that the elements of cards are not necessarily sorted in ascending order.
4)

{118, 321, 322, 119, 120, 320}
Returns: 4
5)

{10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9}
Returns: 7
"""
class SRMCards:
  def maxTurns(self, cards):
    ce = [1]*len(cards)
    cards = sorted(cards)
    while i < len(cards):


if __name__ == '__main__':
  print SRMCards().maxTurns((10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9))
  print SRMCards().maxTurns((99, 100, 98, 239, 73, 294, 240, 71, 293, 74,
    292, 348, 72, 347, 350, 291, 237, 238, 349))
