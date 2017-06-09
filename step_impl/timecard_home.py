import re
import atx
import time
from getgauge.python import *
from step_impl.support import swipe_to

driver = None


@before_spec
def device_set_up():
    global driver
    driver = atx.connect('http://localhost:8100')
    driver.start_app()


@before_scenario
def reload():
    driver(text='ReloadButton').click()
    time.sleep(5)


@before_step
def wait_enough_time(context):
    p = re.compile('^I should')
    if p.match(context.step.text):
        time.sleep(5)


@step("I go to previous week")
def go_to_previous_week():
    driver.click_image('images/previous.1334x750.png', timeout=3)


@step("I go to following week")
def go_to_following_week():
    driver.click_image('images/following.1334x750.png', timeout=3)


@step("I should see <number> approved timecards")
def should_have_how_many_approved_timecards(number):
    assert str(driver(text='Approved').count) == number


@step("I should see <number> entries")
def should_have_how_many_entry(number):
    assert str(driver(text='PROJECT/ASSIGNMENT').count) == number


@step("I click <text>")
def click_by_text(text):
    element = driver(text=text)
    swipe_to(driver, element)
    element.click()


@step(["I should see a dialogue <message>", "I should see a message <message>"])
def should_have_right_dialogue(message):
    assert driver(text=message).exists is True


@step("I delete the entry at index <idx>")
def delete_timecard_entry(idx):
    idx = int(idx)
    swipe_to(driver, driver(text='PROJECT/ASSIGNMENT', index=idx - 1))
    b = driver(text='delete', index=idx - 1).bounds
    x, y, w, h = b.x, b.y, b.width, b.height
    s = driver.scale
    driver.click(s * (x - w / 2), s * (y + h / 2))
