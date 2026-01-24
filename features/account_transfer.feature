Feature: Money transfers
    
    Scenario: User can perform successful transfer between accounts
        Given Account registry is empty
        And I create an account using name: "tomasz", last name: "lis", pesel: "75010122334"
        And Account with pesel "75010122334" has balance: "2000"
        And I create an account using name: "ewa", last name: "zlotowska", pesel: "68050599887"
        And Account with pesel "68050599887" has balance: "100"
        When I transfer "500" from account "75010122334" to account "68050599887"
        Then Account with pesel "75010122334" has balance: "1500"
        And Account with pesel "68050599887" has balance: "600"

    Scenario: Transfer fails when insufficient funds
        Given Account registry is empty
        And I create an account using name: "tomasz", last name: "lis", pesel: "75010122334"
        And Account with pesel "75010122334" has balance: "100"
        And I create an account using name: "ewa", last name: "zlotowska", pesel: "68050599887"
        And Account with pesel "68050599887" has balance: "500"
        When I attempt to transfer "200" from account "75010122334" to account "68050599887"
        Then Transfer should fail with error "Invalid withdraw amount"
        And Account with pesel "75010122334" has balance: "100"
        And Account with pesel "68050599887" has balance: "500"

    Scenario: Transfer fails when sender account does not exist
        Given Account registry is empty
        And I create an account using name: "ewa", last name: "zlotowska", pesel: "68050599887"
        When I attempt to transfer "100" from account "12345678901" to account "68050599887"
        Then Transfer should fail with error "Account not found"

    Scenario: Express transfer with fee
        Given Account registry is empty
        And I create an account using name: "tomasz", last name: "lis", pesel: "75010122334"
        And Account with pesel "75010122334" has balance: "2000"
        When I make express transfer of "500" from account "75010122334"
        Then Account with pesel "75010122334" has balance: "1499"