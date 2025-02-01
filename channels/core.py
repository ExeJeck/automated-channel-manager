from . import config
from .channels_management import ChannelsManagement


class Core():
    def __init__(self):
        pass


    def main(self):
        channel_management = ChannelsManagement()
        channel_management.channels_management_logic()
