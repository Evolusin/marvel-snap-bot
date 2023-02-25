class Gameboard:
    """Class representing a game board with 3 boards, each with 4 card slots."""

    def __init__(self):
        """Initialize three empty game boards."""
        self.boards = [[""] * 4 for _ in range(3)]

    def add_card(self, board_idx, card):
        """
        Add a card to the specified board if there is space.

        Args:
            board_idx (int): Index of the board to add the card to.
            card (str): The card to add to the board.

        Returns:
            bool: True if the card was added successfully, False otherwise.
        """
        for i, card_slot in enumerate(self.boards[board_idx]):
            if not card_slot:
                self.boards[board_idx][i] = card
                return True
        return False

    def remove_card(self, board_idx, card_idx):
        """
        Remove a card from the specified board.

        Args:
            board_idx (int): Index of the board to remove the card from.
            card_idx (int): Index of the card to remove.

        Returns:
            None
        """
        try:
            self.boards[board_idx][card_idx] = ""
        except (IndexError, TypeError):
            print(
                f"Invalid board or card index provided: board={board_idx},"
                f" card={card_idx}"
            )

    def count_free_slots(self):
        """
        Count the number of free slots on all boards.

        Returns:
            int: The number of free slots on all boards.
        """
        count = 0
        for board in self.boards:
            count += board.count("")
        return count

    def count_free_slots_on_board(self, board_idx):
        """
        Count the number of free slots on specifict boards.

        Args:
            board_idx (int): Index of the board to check free slots.

        Returns:
            int: The number of free slots on all boards.
        """
        return self.boards[board_idx].count("")
