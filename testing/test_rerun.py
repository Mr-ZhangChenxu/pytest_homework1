from time import sleep

import pytest


def test_a():
    sleep(0.5)
    assert 1==1

def test_b():
    sleep(0.5)
    assert 1==2

@pytest.mark.flaky(reruns=5)
def test_c():
    sleep(0.5)
    assert 3==1
