class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.equal_scores()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.score_at_least_four()

        else:
            score = self.standard_scoring()

        return score

    def equal_scores(self):
        score_names = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        if self.m_score1 <= 2:
            return score_names[self.m_score1]
        return score_names[3]

    def score_at_least_four(self):
        score_diff = self.m_score1 - self. m_score2
        advantage = {-1: "Advantage player2", 1: "Advantage player1"}
        if score_diff < 0:
            return advantage[score_diff] if score_diff == -1 else "Win for player2"
        return advantage[score_diff] if score_diff == 1 else "Win for player1"

    def standard_scoring(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.m_score1]}-{score_names[self.m_score2]}"

