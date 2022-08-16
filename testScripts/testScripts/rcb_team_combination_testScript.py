import json
import unittest

import pytest

# read the provided team details
with open('rcbTeamDetails.json') as f:
    rcb_team_details = json.load(f)
    team_size = len(rcb_team_details['player'])


class TeamCombination(unittest.TestCase):

    @pytest.mark.order(1)
    def test_total_no_of_players(self):

        # Verify that total number of players should be 11
        self.assertEqual(team_size, 11)

    @pytest.mark.order(2)
    def test_no_of_foreign_players(self):
        # Verify that number of foerign players should not exceed 4
        total_no_of_foreign_players = 0
        for i in range(team_size):
            players_country = str(rcb_team_details['player'][i]['country'])
            if players_country.lower() != 'india':
                total_no_of_foreign_players = total_no_of_foreign_players + 1
        self.assertLessEqual(total_no_of_foreign_players, 4)

    @pytest.mark.order(3)
    def test_no_of_wicket_keepers(self):
        # Verify that there should be atleast one wicket-keeper in the team
        total_no_of_wk = 0
        for i in range(team_size):
            players_role = str(rcb_team_details['player'][i]['role'])
            if players_role.lower() == 'wicket-keeper':
                total_no_of_wk = total_no_of_wk + 1
        self.assertGreaterEqual(total_no_of_wk, 1)


if __name__ == '__main__':
    unittest.main()
