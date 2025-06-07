cards = input().split(" ")
cards_set = set(cards)
cards_list = list(cards_set)

starting_players_team_a = 11
starting_players_team_b = 11

team_a_cards_received = 0
team_b_cards_received = 0

game_is_terminated = False

for current_card in range(len(cards_list)):

    if 'A' in cards_list[current_card]:
        team_a_cards_received += 1

    elif 'B' in cards_list[current_card]:
        team_b_cards_received += 1

    if team_a_cards_received == 5 or team_b_cards_received == 5:
        game_is_terminated = True
        break

team_a_players_left = starting_players_team_a - team_a_cards_received
team_b_players_left = starting_players_team_b - team_b_cards_received

print(f"Team A - {team_a_players_left}; Team B - {team_b_players_left}")

if game_is_terminated:
    print("Game was terminated")