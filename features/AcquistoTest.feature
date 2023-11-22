Feature: Acquisto prodotti

  Come cliente
  Voglio poter fare acquisti online
  Per poter comprare i prodotti da casa

  Scenario: Acquisto un prodotto
    Given I logged into my account
    When I add to the cart a "Sauce Labs Backpack"
    Then I can checkout the order