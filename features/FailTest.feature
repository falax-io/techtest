Feature: Il prezzo del prodotto è corretto

  Come cliente
  Voglio controllare che il prezzo sia giusto
  Per essere sicuro di non stare pagando più del dovuto

  Scenario: KO VOLUTO - Prezzo in fase di checkout corretto
    Given I logged into my account
    When I add to the cart a "Sauce Labs Onesie"
    Then the price showed in the checkout page is "Totale sbagliato"
