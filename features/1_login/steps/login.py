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
