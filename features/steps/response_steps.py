from behave import given, then, when
from src.main.endpoint_reader import get_response


@given(u"there is a user with token '{token_value}'")
def given_user_with_token(context, token_value):
    context.token = token_value


@when(u'user gets data from endpoint')
def when_user_gets_data(context):
    context.response = get_response(context.token)


@then(u"user gets status code '{status_code}'")
def then_user_gets_status_code(context, status_code: int):
    assert int(status_code) == context.response.status_code


@then(u"response contains authenticated equal '{auth_value}'")
def then_user_gets_authenticated_value(context, auth_value: bool):
    context.response_data = context.response.json()
    assert bool(auth_value) == context.response_data['authenticated']


@then(u"response token corresponds to the request token")
def then_tokens_match(context):
    print(context.token[7:])
    print(context.response_data['token'])
    assert context.token[7:] == context.response_data['token']
