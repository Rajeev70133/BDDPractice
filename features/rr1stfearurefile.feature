Feature: Astroyogi Kundali match
  Scenario: Astroyogi Kundali match success on valid data set
    Given Launch chrome browser
    And open Astroyogi Kundaliform page
    And Enter valid details in all the fileds of
    And Click on Get Your Kundali button
    When Astroyogi KundaliResult page is open
    Then verify that the ResultTable is present on result page
    And close browser