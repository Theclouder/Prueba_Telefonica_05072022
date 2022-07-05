Feature: Test the python searching program

    Scenario Outline: Find information with the name <name>
        When I search <name> in the API and check if it is <result>
        Then I get the lists which have this name: <name>

    Examples:
    |     name    |                                                             result                                                                                                                      |
    |   El Mundo  | {"Name": "El Mundo", "Type": "Daily newspaper", "Language": ["Spanish"], "Owner": "Unidad Editorial S.A.", "Website": "http://www.elmundo.es", "Country": "Spain"}                      |
    |   El Pais   | {"Name": "El Pais", "Type": "Daily newspaper", "Language": ["Spanish", "Portuguese", "Catalan", "English"], "Owner": "PRISA", "Website": "http://www.elpais.com", "Country": "Spain"}   |