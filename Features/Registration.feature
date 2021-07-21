Feature: Verifying registration functionality

  @Sanity
  Scenario: Registration with valid data
    Given User open browser, enter URL and navigate to login page
    When  User enters username
    And   User enters email and address
    And   User enters password
    And   User click on signup button
    Then  User should register successfully

  @Sanity @Smoke
  Scenario: Registration with duplicate username data
    Given User open browser, enter URL and navigate to login page
    When  User enters duplicate username
    And   User enters password
    And   User click on signup button
    Then  User should register successfully

# To run execute behave with tags, use these following command:
# behave [Folder_Contain_file.feature] - This will execute all scenario in the feature
# behave --tags=[tag_name] [Folder_Contain_file.features] - This will execute all scenario with the specific tags
# behave --tags=[tag_name_1] --tags=[tag_name2] [Folder_Contain_file.features]
# - This will execute all scenario containing 2 tags or more if implemented