from getgauge.python import step, before_scenario, Messages
from urllib.request import urlopen
import json
import atx


@before_scenario()
def before_scenario_hook():
    driver = atx.connect('http://localhost:8100')
    driver.start_app()



def get_entire_page_in_json(app):
    html = urlopen(r'http://localhost:8100/source?format=json')
    res_data = json.loads(html.read())

    if app == 'okta':
        okta = res_data['value']['children'][0]['children'][0]['children'][2]['children'][0]['children'][0] \
            ['children'][0]['children'][0]['children'][1]['children'][0]['children'][0]['children'][0]['children']
        return okta
    else:
        browser = res_data['value']['children'][1]['children'][0]['children'][0]['children'][0]['children'][0] \
            ['children'][0]['children'][1]['children'][0]['children'][0]['children'][0]['children'][0] \
            ['children'][0]['children'][0]['children'][0]['children']
        return browser


def load(file_name):
    with open('../pages/examples/' + file_name) as json_file:
        data = json.load(json_file)
        return data


def list_compare(e, a):
    for i in range(len(e)):
        if not structure_compare(e[i], a[i]):
            return False
    return True


def structure_compare(p, q):
    if p['type'] != q['type']:
        return False
    if p['name'] != q['name']:
        return False
    if 'children' in p and 'children' in q:
        for i in range(len(p['children'])):
            if not structure_compare(p['children'][i], q['children'][i]):
                return False
        return True
    elif 'children' not in p and 'children' not in q:
        return True
    else:
        return False


def swipe_to(driver, element):
    s = driver.scale
    y = element.bounds.y * s
    ww, wh = driver.display
    y = y - wh * 0.6
    while abs(y) > wh * 0.3:
        if y > 0:
            driver.swipe(ww * 0.5, wh * 0.8, ww * 0.5, wh * 0.3)
            y -= wh * 0.48
        else:
            driver.swipe(ww * 0.5, wh * 0.3, ww * 0.5, wh * 0.8)
            y += wh * 0.48
    driver.swipe(ww * 0.5, wh * 0.6, ww * 0.5, wh * 0.6 - y)