*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Username too short

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Page Should Contain  Password too short

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Credentials
    Page Should Contain  Password must not consist of only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Submit Credentials
    Page Should Contain  Password confirmation does not match

Register With Username That Is Already In Use
    Set Username  kallekalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Username already exists

Login After Successful Registration
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Welcome to Ohtu Application!
    Go To User Page
    Click Button  Logout
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Page Should Contain  Ohtu Application main page

Login After Failed Registration
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Page Should Contain  Username too short
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Click Button  Login
    Page Should Contain  Invalid username or password


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kallekalle  kalle123
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}