import numpy as np

states = ["rainy", "cloudy", "sunny"]
actions = ["umbrella", "none"]
rewards = np.zeros(shape=(len(states), len(actions)))
rewards[states.index("rainy"), actions.index("umbrella")] = 1
rewards[states.index("rainy"), actions.index("none")] = -1
rewards[states.index("sunny"), actions.index("umbrella")] = -1
rewards[states.index("sunny"), actions.index("none")] = 1

history = []

n_steps = 100
learning_rate = 0.01
discount_factor = 0.5
Q = np.zeros(shape=(len(states), len(actions)))

def update_Q(state, action, reward):
    i = states.index(state)
    j = actions.index(action)
    m = np.max(Q[j,])
    Q[i,j] = (1-learning_rate) * Q[i,j] + learning_rate * (reward + discount_factor * m)

def print_report():
    for i in range(len(states)):
        state = states[i]
        action_idx = np.argmax(Q[i,])
        action = actions[action_idx]
        print("My thoughts?   {s} -> {a}  ({p})".format(s=state, a=action, p=Q[i,action_idx]))

print_report()

for step in range(n_steps):
    state = np.random.choice(states,1)[0]
    action_idx = np.argmax(Q[states.index(state),])
    action = actions[action_idx]
    reward = rewards[states.index(state), actions.index(action)]

    #best_action_idx = np.argmax(Q[states.index(state),])
    #best_action = actions[best_action_idx]

    history.append([state,action, reward])
    update_Q(state, action, reward)
    #print("{s} -> {a}  =  {r}".format(s=state, a=action, r=reward))
    #print("Today is {s} and so I chose {a} and got {r}.\n The best thing to do would have been {b}."
    #    .format(s=state, a=action, r=reward, b=best_action))

#print("Q is now")
#print(Q)
print("...")
print_report()
