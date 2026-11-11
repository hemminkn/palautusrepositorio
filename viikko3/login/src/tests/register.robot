*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Matching Password And Confirmation
    Set username  kille
    Set password and confirmation  kille321  kille321
    Click  button >> text=Register
    Registering Should Succeed

Register With Different Password And Confirmation
    Set username  kille
    Set password and confirmation  kille321  kalle321
    Click  button >> text=Register
    Registering Should Fail With Message  Password and confirmation do not match

Register With Too Short Username And Valid Password
    Set username  ki
    Set password and confirmation  kille321  kille321
    Click  button >> text=Register
    Registering Should Fail With Message  Username should be 3 or more characters

Register With Valid Username And Too Short Password
    Set username  kille
    Set password and confirmation  kille32  kille32
    Click  button >> text=Register
    Registering Should Fail With Message  Password should be 8 or more characters

Register With Password Containing Numbers
    Set username  kille
    Set password and confirmation  kalle123  kalle123
    Click  button >> text=Register
    Registering Should Succeed

Register With Password Containing Special Characters
    Set username  kille
    Set password and confirmation  kalle#abc  kalle#abc
    Click  button >> text=Register
    Registering Should Succeed

Register With Password Containing Only Lowercase Letters
    Set username  kille
    Set password and confirmation  kallekalle  kallekalle
    Click  button >> text=Register
    Registering Should Fail With Message  Password should contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set username  kille
    Set password and confirmation  KalleKalle  KalleKalle
    Click  button >> text=Register
    Registering Should Fail With Message  Password should contain at least one non-letter character

Register With Username That Is Already In Use

    Set username  kille
    Set password and confirmation  kille321  kille321
    Click  button >> text=Register
    Registering Should Succeed
    Go To Main Page
    Click  button >> text=Logout
    Go To Register Page
    Set username  kille
    Set password and confirmation  kille123  kille123
    Click  button >> text=Register
    Registering Should Fail With Message  User with username kille already exists

*** Keywords ***
Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password And Confirmation
    [Arguments]  ${password}  ${confirmation}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $confirmation

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
