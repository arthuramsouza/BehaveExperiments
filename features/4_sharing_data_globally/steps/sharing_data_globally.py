from behave import *

use_step_matcher("re")


@given("I find recent order from database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Finding an order from the database...')
    context.order_number = '112233'
    print('Found an order! Order number: ' + context.order_number)


@when("I issue a refund for the order")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Trying to issue a refund for order number ' + context.order_number)


@then("the payment gets processed by the user")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Payment successfully processed!')
    print('The payment is for a refund for the order number ' + context.order_number)
