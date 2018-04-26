Feature: Verify a Google certificate

  Scenario Outline: As a Third Party User I would like to verify a certificate expended by Google
    Given A <google certificate title> Google certificate
     When I navigate the <certificate key> certificate page
      And I select Verify option
     Then The certificate is verified block chain
      And The title of certificate is <google certificate title>

    Examples: Google certificate keys
      | google certificate title       | certificate key |
      | Professional - Cloud Architect | a6ua4dds        |