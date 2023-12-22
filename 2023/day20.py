with open('day20', 'r') as f:
    file = f.read().split('\n')

modules = {}
for line in file:
    source, destination = line.split(' -> ')
    modules[source[1:]] = [source[0], destination.split(', ')]

states = {}
for name, (module, _) in modules.items():
    if module == 'b':
        states[name] = '-'
    if module == '%':
        states[name] = 'off'
    if module == '&':
        states[name] = {}

for source, (_, destinations) in modules.items():
    for destination in destinations:
        if destination in modules:
            if modules[destination][0] == '&':
                states[destination][source] = 'low'

pushes = 0
goal = 1000000
invert = {'on': 'off', 'off': 'on'}
invert_pulse = {'high': 'low', 'low': 'high'}
memory = {}
pulse_count = {'high': 0, 'low': 0}
cycle_found = False
start_state_hash = hash(str(states))


def send(queue, pulse_count, pulse, sent_to):
    for destination in sent_to:
        # print(pulse, 'to', destination)
        pulse_count[pulse] += 1
        if destination == 'rx' and pulse == 'low':
            print(pushes)
            exit(0)
        if destination in modules:
            queue.append([destination, pulse, receiver])
    return queue, pulse_count


def predict(goal, pushes, pulse_count):
    res = 1
    for pulse, count in pulse_count.items():
        res *= count * goal / pushes
    print(res)


while pushes < goal:
    pushes += 1
    queue = [('roadcaster', 'low', 'button')]
    pulse_count['low'] += 1
    while len(queue) > 0:
        receiver, pulse, sender = queue.pop(0)
        state = states[receiver]
        module, sent_to = modules[receiver]

        if module == 'b':
            queue, pulse_count = send(queue, pulse_count, pulse, sent_to)
        if module == '%' and pulse == 'low':
            states[receiver] = invert[state]
            pulse = 'high' if states[receiver] == 'on' else 'low'
            queue, pulse_count = send(queue, pulse_count, pulse, sent_to)
        if module == '&':
            states[receiver][sender] = pulse
            if len(set(states[receiver].values())) == 1 and pulse == 'high':
                pulse = invert_pulse[pulse]
                queue, pulse_count = send(queue, pulse_count, 'low', sent_to)
            else:
                queue, pulse_count = send(queue, pulse_count, 'high', sent_to)
    hash_of_state = hash(str(states))
    if hash_of_state == start_state_hash:
        print('cycle found', pushes)
        predict(goal, pushes, pulse_count)
        print(pulse_count, pulse_count['low'] * pulse_count['high'])
        break
print(pulse_count, pulse_count['low']*pulse_count['high'])
