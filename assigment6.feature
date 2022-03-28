Feature: Python.org Searching
  As a python dev, I want to search python.org, so that I can learn features of python

Scenario: Search for "list comprehension" is entered
    Given I am on the python.org homepage
    When I enter the search "list comprehension"
    Then Search results are displayed