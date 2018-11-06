from behave import given


@given("I have a new '{item}' in my cart")
def item_in_cart(context, item):

    if item.lower() not in ['book', 'dvd']:
        raise Exception('Unexpected text passed as item.')

    print("The item is: {}".format(item))

    if item.lower() == 'book':
        print('Go read it!')
    elif item.lower() == 'dvd':
        print('GO watch it!')
