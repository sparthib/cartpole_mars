from gym.envs.registration import register


register(
    id='cartpolemars-v0',
    entry_point='cartpole_mars.envs:CartPoleEnv')

# tags={'wrapper_config.TimeLimit.max_episode_steps': 500},
#reward_threshold=475.0
