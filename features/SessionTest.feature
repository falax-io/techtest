Feature: Sessione

  Come cliente
  Voglio essere sicuro di aver effettuato correttamente il logout
  Per evitare che qualcun altro possa usare il mio account

  Scenario: Logout e rinavigazione
    Given I logged into my account
    When I logout from my account
    Then I cannot navigate trough the website