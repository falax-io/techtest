from behave import *

from features.models.pages.cart_page import CartPage
from features.models.pages.checkout_complete import CheckoutCompletePage
from features.models.pages.checkout_step_one_page import CheckoutStepOnePage
from features.models.pages.checkout_step_two_page import CheckoutStepTwoPage
from features.models.pages.common_page import CommonPage
from features.models.pages.index_page import IndexPage
from features.models.pages.inventory_page import InventoryPage


@given("I logged into my account")
def step_impl(context):
    page = context.page
    page.goto("https://www.saucedemo.com/")
    context.page = page
    index_page = IndexPage(page)
    index_page.login("standard_user", "secret_sauce")


@when('I add to the cart a "{item_name}"')
def step_impl(context, item_name):
    inventory_page = InventoryPage(context.page)
    inventory_page.add_item_to_cart(item_name)
    inventory_page.click_cart()
    cart_page = CartPage(context.page)
    cart_page.click_checkout()


@then("I can checkout the order")
def step_impl(context):
    checkout_step_one_page = CheckoutStepOnePage(context.page)
    checkout_step_one_page.fill_the_form("Test", "Test", "12345")
    checkout_step_one_page.click_continue()
    checkout_step_two_page = CheckoutStepTwoPage(context.page)
    checkout_step_two_page.click_finish()
    checkout_complete_page = CheckoutCompletePage(context.page)
    assert checkout_complete_page.is_checkout_complete() is True


@then('the price showed in the checkout page is "{total}"')
def step_impl(context, total):
    checkout_step_one_page = CheckoutStepOnePage(context.page)
    checkout_step_one_page.fill_the_form("TestA", "TestB", "12345")
    checkout_step_one_page.click_continue()
    checkout_step_two_page = CheckoutStepTwoPage(context.page)
    actual_total = checkout_step_two_page.get_total_dollars()
    assert actual_total == total is True


@when("I logout from my account")
def step_impl(context):
    common_page = CommonPage(context.page)
    common_page.click_hamburger_menu()
    common_page.click_logout()


@then("I cannot navigate trough the website")
def step_impl(context):
    context.page.goto("https://www.saucedemo.com/inventory.html")
    index_page = IndexPage(context.page)
    assert index_page.is_error_displayed() is True
