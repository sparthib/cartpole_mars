from gym.envs.registration import register


register(
    id='cartpolemars-v0',
    entry_point='cartpole_mars.envs:CartPoleEnv')

register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='cartpole_mars.envs:FrozenLakeEnv',
    kwargs={'map_name' : '8x8', 'is_slippery': False},
)
