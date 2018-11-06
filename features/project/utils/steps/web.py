import logging
from behave import given
from features.project.utils.functions import web

logging.basicConfig(level='INFO')


@given('I go to the site')
def go_to_url(context, url):
    """
    Step definition to go to the specified url
    :param context:
    :param url: address to navigate to
    """
    logging.info("Navigating to the site: " + url)
    context.driver = web.go_to(url)
