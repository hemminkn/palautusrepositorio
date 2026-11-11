*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set username  kille
    Set password  kille321
    Click  button >> text=Register
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set username  ki
    Set password  kille321
    Click  button >> text=Register
    Registering Should Fail With Message  Username should be 3 or more characters

Register With Valid Username And Too Short Password
    Set username  kille
    Set password  kille32
    Click  button >> text=Register
    Registering Should Fail With Message  Password should be 8 or more characters

Register With Username That Is Already In Use
# user with username kille already exists

    Set username  kille
    Set password  kille321
    Click  button >> text=Register
    Registering Should Succeed
    Go To Main Page
    Click  button >> text=Logout
    Go To Register Page
    Set username  kille
    Set password  kille123
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

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
