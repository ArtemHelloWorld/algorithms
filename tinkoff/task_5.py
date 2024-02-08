def count_states(roads_lst, validator=0):
    states = []
    for road in roads_lst:
        town_a, town_b = road[0], road[1]

        state_a, state_b = None, None
        for state in states:
            if town_a in state:
                state_a = state
            if town_b in state:
                state_b = state
            if state_a and state_b:
                break

        if road[2] > validator:
            if not state_a and not state_b:
                states.append({town_a, town_b})
            elif state_a and not state_b:
                state_a.add(town_b)
            elif state_b and not state_a:
                state_b.add(town_a)
            elif state_a and state_b and state_a != state_b:
                state_a.update(state_b)
                states.remove(state_b)
        else:
            if not state_a:
                states.append({town_a})
            if not state_b:
                states.append({town_b})

    return len(states)


towns_count, roads_count = tuple(map(int, input().split()))

roads = []
length = set()
for _ in range(roads_count):
    road = tuple(map(int, input().split()))
    roads.append(road)
    length.add(road[2])

start_states_count = count_states(roads)

for length_i in sorted(length):
    c = count_states(roads, length_i)
    if c != start_states_count:
        print(length_i - 1 )
        break
