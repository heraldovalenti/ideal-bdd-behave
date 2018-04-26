from behave import given, when, then

from features.pages.credential_net_page import CredentialNetPage


@given("A {certificate_title} certificate")
def given_the_certificate(context, certificate_title):
    context.certificate_title = certificate_title


@when("I navigate the {certificate_key} certificate page")
def navigate_certificate_key(context, certificate_key):
    driver = context.driver
    credential_net_page = CredentialNetPage(driver)
    context.credential_net_page = credential_net_page
    credential_net_page.navigate_certificate_key(certificate_key)


@when("I select {option} option")
def select_option(context, option):
    credential_net_page = context.credential_net_page
    credential_net_page.select_option(option)


@then("The certificate is verified block chain")
def certificate_verified(context):
    credential_net_page = context.credential_net_page
    is_certificate_verified = credential_net_page.is_certificate_verified()
    assert is_certificate_verified


@then("The title of certificate is {certificate_title}")
def verify_certificate_title(context, certificate_title):
    credential_net_page = context.credential_net_page
    actual_title = credential_net_page.certificate_title()
    assert (certificate_title in actual_title)
