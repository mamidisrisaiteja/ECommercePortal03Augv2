@inventory @smoke
Feature: Product Inventory Management
  As a user
  I want to view and interact with the product inventory
  So that I can see available products and add them to cart

  Background:
    Given user is on Login Page
    When user enters user name as "standard_user" and password as "secret_sauce"
    And click Login Button
    Then verify page has text "Products"

  @inventory_view
  Scenario: View product inventory
    Given user is on products page
    When user views the product list
    Then user should see multiple products available

  @add_to_cart
  Scenario: Add product to cart
    Given user is on products page
    When user adds "sauce-labs-backpack" to cart
    Then cart should show 1 item
