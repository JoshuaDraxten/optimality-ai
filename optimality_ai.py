import random


class Optimality:
    def __init__(self, play_game, generate_move_candidates, flip_game, verbose=False):
        """
            play_game function must return an array of every move made
            generate_move_candidates takes a board and returns candidates of movments that can be made
            flip_game takes an array of moves and makes them
        """
        self.win_examples = []
        self.lose_examples = []
        self.play_game = play_game
        self.generate_move_candidates = generate_move_candidates
        self.flip_game = flip_game
        self.verbose = verbose

    def log(self, str):
        if self.verbose:
            print(str)

    def set_constraints(self, constraints):
        self.constraints = constraints

    def evaluate_candidates(self, candidates):
        passing_candidates = candidates.copy()
        for constraint in self.constraints:
            # Score every candidate based on the candidates
            scores = [(int(constraint(candidate)))
                      for candidate in passing_candidates]
            max_score = max(scores)
            # Count backwards and remove any candidate that doesn't reach the max score
            for idx in range(len(passing_candidates)-1, 0, -1):
                if scores[idx] != max_score:
                    passing_candidates.pop(idx)
        return passing_candidates

    def log_tableau(self, candidates):
        """
            Used for debugging
        """
        tableau = []
        for constraint in self.constraints:
            self.log("\t".join([constraint.__name__] + [str(int(constraint(candidate)))
                                                        for candidate in candidates]))
        return tableau

    def sort_constraints(self):
        """
            TODO This is the machine learning bit
        """
        if len(self.lose_examples) == 0:
            return self.constraints

        last_loss = self.lose_examples[-1]
        novel_winning_game = self.flip_game(last_loss)

        # Get last prediction

        return self.constraints

    def generate_next_move(self, board):
        """
            Uses the supplied generate_move_candidates function and picks the optimal one
            If there are multiple equally optimal moves, it returns one of them randomly
        """
        possible_moves = self.generate_move_candidates(board)
        candidates = self.evaluate_candidates(possible_moves)
        return candidates[random.randint(0, len(candidates)-1)]

    def train(self):
        """
            Run the game several times to train the AI
        """
        winning_streak = 0
        # TODO: Include a better way to determine when to stop the training
        while winning_streak < 5:
            game = self.play_game(self.generate_next_move)
            if game["winner"] == 1:
                winning_streak += 1
                self.win_examples.append(game["moves"])
            elif game["winner"] == -1:
                winning_streak = 0
                # Player did well so we want to learn from what they did
                self.lose_examples.append(game)
            else:
                continue
                # For now, we don't do anything with a cats game
            self.constraints = self.sort_constraints()
