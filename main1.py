import sys
import numpy as np
import math
import random
import gym
import gym_game


if __name__ == "__main__":
    env = gym.make("Pygame-v0")
    observation = env.reset()
    for i in range(1000):
        action = env.action_space.sample()
        observation, reward, done, truncated, info = env.step(action)
        env.render()
