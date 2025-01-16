import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from util import filter_first, filter_last, filter_timestamps, filter_ipv4, filter_ipv6

@pytest.fixture
def log_lines():
    return [
        "2023-01-01 12:00:00 This is a log line with a timestamp 12:00:00\n",
        "This line contains an IPv4 address 192.168.0.1\n",
        "This line contains an IPv6 address fe80::1ff:fe23:4567:890a\n",
        "This is just a regular log line\n"
    ]

def test_filter_first(log_lines):
    print("Running test_filter_first")
    assert filter_first(log_lines, 2) == log_lines[:2]

def test_filter_last(log_lines):
    print("Running test_filter_last")
    assert filter_last(log_lines, 2) == log_lines[-2:]

def test_filter_timestamps(log_lines):
    print("Running test_filter_timestamps")
    expected = [log_lines[0]]
    assert filter_timestamps(log_lines) == expected

def test_filter_ipv4(log_lines):
    print("Running test_filter_ipv4")
    expected = ["This line contains an IPv4 address 192.168.0.1\n"]
    assert filter_ipv4(log_lines) == expected

def test_filter_ipv6(log_lines):
    print("Running test_filter_ipv6")
    expected = ["This line contains an IPv6 address fe80::1ff:fe23:4567:890a\n"]
    assert filter_ipv6(log_lines) == expected