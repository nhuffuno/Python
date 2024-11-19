import pytest
from television import Television


class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = MUTED"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()  
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 2, Volume = 0"
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_down()
        self.tv.channel_down()  
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        self.tv.volume_up() 
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_down()
        self.tv.volume_down() 
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_volume_mutes_on_adjust(self):
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = MUTED"
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
