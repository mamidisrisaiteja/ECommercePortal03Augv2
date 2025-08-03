@auth @smoke
Feature: Authentication Module
  As a user
  I want to login to the ecommerce portal
  So that I can access the products

  @TC_AUTH_01
  Scenario: Login with Valid credentials
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"
