Feature: Astroyogi Kundali match
  Scenario: Astroyogi Kundali match success on valid data set
    Given Launch chrome browser
    And open Astroyogi Kundaliform page
    And Enter valid details in all the fileds of
    When Click on Get Your Kundali button to open kundali resulty page
    Then verify that the ResultTable is present on result page
    And close browser