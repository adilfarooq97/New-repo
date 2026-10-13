import datetime
import unittest
from unittest.mock import patch

import pytz

from agent.when_gate import should_post_now


class FrozenDateTime(datetime.datetime):
    @classmethod
    def now(cls, tz=None):
        current = datetime.datetime(2026, 10, 13, 17, 24)
        return tz.localize(current) if tz else current


class TestPostingScheduleGate(unittest.TestCase):
    def setUp(self):
        self.timezone = pytz.timezone("Asia/Karachi")
        self.posting_config = {
            "timezone": "Asia/Karachi",
            "candidate_times": ["10:00"],
            "time_window_end": 300,
        }
        self.datetime_patcher = patch("agent.when_gate.dt.datetime", FrozenDateTime)
        self.datetime_patcher.start()
        self.addCleanup(self.datetime_patcher.stop)
        self.config_patcher = patch("agent.when_gate._load_posting_config",
                                    return_value=self.posting_config)
        self.config_patcher.start()
        self.addCleanup(self.config_patcher.stop)

    @patch("agent.when_gate.storage.get_state", return_value=None)
    def test_delayed_scheduled_run_can_post_after_window(self, _get_state):
        self.assertTrue(should_post_now(scheduled=True))

    @patch("agent.when_gate.storage.get_state", return_value="2026-10-13")
    def test_delayed_scheduled_run_does_not_post_twice_in_one_day(self, _get_state):
        self.assertFalse(should_post_now(scheduled=True))

    @patch("agent.when_gate.storage.get_state", return_value=None)
    def test_regular_run_still_respects_posting_window(self, _get_state):
        self.assertFalse(should_post_now())


if __name__ == "__main__":
    unittest.main()
