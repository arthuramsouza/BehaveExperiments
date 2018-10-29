from behave import given, when, then


@given('I create a new user')
def create_new_user(context):
    """
    Step to create a new user
    :param context:
    :return:
    """
    print('Creating new user')


@when('I type correct email')
def type_correct_email(context):
    """
    Step to type email in the email field
    :param context:
    :return:
    """


@when("I type correct password")
def type_correct_password(context):
    """
    :type context: behave.runner.Context
    """


@when("I click on 'Login'")
def click_login(context):
    """
    :type context: behave.runner.Context
    """


@then("I should see the text 'Welcome'")
def see_text_welcome(context):
    """
    :type context: behave.runner.Context
    """


@given("I generate a random email address")
def generate_random_email(context):
    """
    :type context: behave.runner.Context
    """


@when("I type random email")
def type_random_email(context):
    """
    :type context: behave.runner.Context
    """


@then("I should see the text 'Error: User not found'")
def see_error_user_not_found(context):
    """
    :type context: behave.runner.Context
    """


@when("I type random password")
def type_random_password(context):
    """
    :type context: behave.runner.Context
    """


@then("I should see the text 'Error: Incorrect password'")
def see_error_incorrect_password(context):
    """
    :type context: behave.runner.Context
    """


@then("I should see the text 'Error: Password field is empty'")
def see_error_password_empty(context):
    """
    :type context: behave.runner.Context
    """


@when("I type invalid email format")
def type_invalid_email(context):
    """
    :type context: behave.runner.Context
    """


@then("I should see the text 'Error: Invalid email format'")
def see_error_invalid_email(context):
    """
    :type context: behave.runner.Context
    """


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


@given("I have a new '{item}' in my cart")
def item_in_cart(context, item):

    if item.lower() not in ['book', 'dvd']:
        raise Exception('Unexpected text passed as item.')

    print("The item is: {}".format(item))

    if item.lower() == 'book':
        print('Go read it!')
    elif item.lower() == 'dvd':
        print('GO watch it!')
