import sys
import numpy as np
import math
import random
import gym
import gym_game


if __name__ == "__main__":
    env = gym.make("Pygame-v0")
    observation = env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, done, truncated, info = env.step(action)
        env.render()
        # khi xe nó chạm thì thoát
        # if done:
        #     break
