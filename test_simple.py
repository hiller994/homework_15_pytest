import random
import time

import pytest


def test1(browser):
    pass

def test2(browser):
    pass

def test_mobile_1():
    pass

def test_mobile_2():
    pass

@pytest.mark.fast # где fast, любое слово, по которому будет идти поиск по -m
def test_first():
    time.sleep(1)

@pytest.mark.slow # где slow, любое слово, по которому будет идти поиск по -m
def test_second():
    time.sleep(5)

@pytest.fixture()
def browser():
    "какой нибудь браузер"
    time.sleep(1)

#--------------------------------------------------------
@pytest.fixture() #эту фикстуру мы не используем (решили в test_fail для примера -l использовать другой пример)
def user(browser):
    return random.randint(0,100)


def test_fail():
    user1 = random.randint(0,100)
    user2 = random.randint(0,100)
    assert user1 == user2