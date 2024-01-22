import gym

env = gym.make("Pendulum-v1", render_mode="human")

state = env.reset()
observation, info = env.reset(seed=42)
for _ in range(500):
   action = env.action_space.sample() 
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()
