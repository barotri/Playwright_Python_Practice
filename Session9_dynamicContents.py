from playwright.sync_api import Page, expect
import pytest
#Session 9
#Test load display page
# def test_load_test_diplay(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator('text=Load Delay').click()
#     assert page.url == 'http://uitestingplayground.com/loaddelay'
#     page.locator('text=Button Appering After Delay').click()
#     page.close()
    
# #test ajax data
# def test_ajax_data(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator('text=AJAX Data').click()
#     assert page.url == 'http://uitestingplayground.com/ajax'
#     page.locator('text=Get Data').click()
#     expect(page.locator('div#content')).to_have_text('Data loaded with AJAX get request.')
    
# #test click
# def test_button_changed(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator("//a[text()='Click']").click()
#     assert page.url == 'http://uitestingplayground.com/click'
#     expect(page.locator('.btn-primary')).to_have_text('Button That Ignores DOM Click Event')
#     page.locator('.btn-primary').click()
#     expect(page.locator('.btn-success')).to_have_text('Button That Ignores DOM Click Event')

# def test_scroll(page):
#     page.goto('http://uitestingplayground.com/')
#     page.locator("//a[text()='Scrollbars']").click()
#     assert page.url == 'http://uitestingplayground.com/scrollbars'
#     page.mouse.wheel(0, 500)
#     expect(page.locator('.btn-primary')).to_have_text('Hiding Button')
#     page.locator('.btn-primary').click()