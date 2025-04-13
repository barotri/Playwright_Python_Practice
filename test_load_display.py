

def load_test_diplay(page):
    page.goto('http://http://uitestingplayground.com/')
    page.locator('text=Load Delay').click()
    assert page.url == 'http://uitestingplayground.com/loaddelay'
    page.locator('text=Button Appering After Delay').click()