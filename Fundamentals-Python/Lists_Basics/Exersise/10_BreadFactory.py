events = input().split('|')

current_energy = 100
current_coins = 100
all_events_are_handled = True

for current_event in events:
    split_event = current_event.split('-')
    event_type = split_event[0]
    event_value = int(split_event[1])

    if event_type == "rest":
        initial_energy = current_energy
        current_energy += event_value

        if current_energy > 100:
            current_energy = 100

        energy_gain = current_energy - initial_energy
        print(f"You gained {energy_gain} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_type == "order":

        if current_energy >= 30:
            current_energy -= 30
            current_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        ingredient = event_type
        coins_to_spend = event_value

        if current_coins - coins_to_spend >= 0:
            current_coins -= coins_to_spend
            print(f"You bought {ingredient}.")

        else:
            print(f"Closed! Cannot afford {ingredient}.")
            all_events_are_handled = False
            break

if all_events_are_handled:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")

