Feature: response parsing

    Scenario: successful authentication
        Given there is a user with token 'Bearer A'
        When user gets data from endpoint
        Then user gets status code '200'
        And response contains authenticated equal 'True'
        And response token corresponds to the request token

    Scenario: failed authentication
        Given there is a user with token 'Bearer ABC'
        When user gets data from endpoint
        Then user gets status code '403'
        And response contains authenticated equal 'False'
        And response token corresponds to the request token
