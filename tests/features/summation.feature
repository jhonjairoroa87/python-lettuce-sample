Feature: Compute summation

    We'll implement summation

    Scenario: Summation of 0
        Given I have the number 0
        When I compute its summation
        Then I see the number 0

    Scenario: Factorial of 1
        Given I have the number 1
        When I compute its summation
        Then I see the number 1

    Scenario: Factorial of 2
        Given I have the number 2
        When I compute its summation
        Then I see the number 3

    Scenario: Factorial of 3
        Given I have the number 3
        When I compute its summation
        Then I see the number 6

    Scenario: Factorial of 4
        Given I have the number 4
        When I compute its summation
        Then I see the number 10

     Scenario: Factorial of 5
        Given I have the number 5
        When I compute its summation
        Then I see the number 15