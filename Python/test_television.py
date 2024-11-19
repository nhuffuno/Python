import pytest
from television import Television


class TestTelevision:
    def setup_method(self):
        """Setup a new Television instance before each test."""
        self.tv = Television()

    def teardown_method(self):
        """Tear down the Television instance after each test."""
        del self.tv

    def test_init(self):
        """Test the initialization of the Television object."""
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        """Test toggling the power of the Television."""
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        """Test muting and unmuting the Television."""
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = MUTED"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_up(self):
        """Test increasing the channel."""
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()  # Loop back to MIN_CHANNEL
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        """Test decreasing the channel."""
        self.tv.power()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 2, Volume = 0"
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_down()
        self.tv.channel_down()  # Loop back to MAX_CHANNEL
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        """Test increasing the volume."""
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        self.tv.volume_up()  # Should remain at MAX_VOLUME
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        """Test decreasing the volume."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_down()
        self.tv.volume_down()  # Should remain at MIN_VOLUME
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_volume_mutes_on_adjust(self):
        """Test that adjusting volume unmutes the Television."""
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = MUTED"
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
