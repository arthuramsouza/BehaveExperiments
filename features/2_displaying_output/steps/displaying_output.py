from behave import given, when, then


@given("I am at the home page")
def at_home_page(context):
    """
    :type context: behave.runner.Context
    """
    print('Code that opens the browser and goes to the home page')


@when("I click on 'Contact us'")
def click_contact_us(context):
    """
    :type context: behave.runner.Context
    """
    print('Clicking on "contact us"')


@then("I should see '123 Testing St.'")
def see_address(context):
    """
    :type context: behave.runner.Context
    """
    print('See the correct address')


@when("I click on my account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Click on "my account"')


@then("I should see 'Preferences'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('See "preferences"')
    assert 1 == 2, "one is not the same as two"
