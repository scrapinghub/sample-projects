# Below is sample code for sending alerts via an ASN Email service
# If you wish to alert through another means such as slack, text, etc replace this section with the appropiate code

import boto
from jinja2 import Environment, PackageLoader

from w3lib.html import remove_tags
import logging
logger = logging.getLogger(__name__)

jinja_env = Environment(loader=PackageLoader('price_monitor', 'alert_template'))

# settings for Amazon SES email service
AWS_ACCESS_KEY = 'AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'AWS_ACCESS_KEY'
EMAIL_ALERT_FROM = 'Price Monitor <SENDER_EMAIL@provider.com>'
EMAIL_ALERT_TO = ['RECEIVER_EMAIL@provider.com']


def send_alert(items):
    ses = boto.connect_ses(AWS_ACCESS_KEY, AWS_SECRET_KEY)
    html_body = jinja_env.get_template('email.html').render(items=items)

    ses.send_email(
        EMAIL_ALERT_FROM,
        'Price drop alert',
        remove_tags(html_body),
        EMAIL_ALERT_TO,
        html_body=html_body
    )