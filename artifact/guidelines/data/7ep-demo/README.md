# 7ep-demo

## Resources

|   |   |
|---|---|
|__GitHub Repository__| https://github.com/SarahBornais/demo |
|__Pre-Built Files__| [/builds](./builds/) |



## Requirements

Java version 11 or greater

## Introduction

The 7ep-demo application was made specifically to demonstrate good software development and testing practices. It features a web-based UI that allows users to interact with a library system, where they can add books and borrowers, and then allow borrowers to check out books (see screenshot below). It also exposes some math-themed API endpoints such an endpoint to calculate two numbers or a Fibonacci sequence.

![image](../images/7ep-demo.png)

### Directory Structure

All relevant application source code is located in `src/main`. There are a variety of tests located in the `src` directory. See the directory outline below for more details. The repository's main `README` file also contains more details on how to run build and run specific features.

```
├── desktop_app              : a project to demonstrate testing of desktop apps
├── docs                     : documents related to this application
├── gradle                   : necessary wrapper files and some capabilities related to certain tests
├── jenkins                  : holds the Jenkinsfile for CI/CD
└── src                      : has the application's source code and all test code
    ├── main                 : code for the application
    │   ├── authentication   : things like usernames, passwords, accounts
    │   ├── cartesianproduct : calculating the cartesian product of multiple sets
    │   ├── expenses         : calculating restaurant expenses
    │   ├── helpers          : cross-functional helper classes
    │   ├── library          : books, borrowers, lending
    │   ├── mathematics      : various math functionality
    │   ├── persistence      : provides database access
    │   └── tomcat           : configures Tomcat
    ├── bdd_test             : tests that use Cucumber to test at the feature level
    ├── integration_test     : primarily tests that hit the database, but really any integration test
    ├── selenified_tests     : tests that use Selenified
    ├── test                 : unit tests
    ├── api_tests            : tests that target the API's
    └── ui_tests             : tests that target the UI
        ├── behave           : files for the Python-based Behave BDD framework
        ├── python           : Python Selenium tests
        ├── js               : JavaScript Selenium tests
        ├── c_sharp          : C# Selenium tests
        └── java             : Java Selenium tests
```

## Instructions

First, clone the forked repository:

```
git clone https://github.com/SarahBornais/demo
cd demo
```

### Building

To build a new jar file: `./gradlew jar`

To build a new war file: `./gradlew war`

The JAR and/or WAR file will be created at `build/libs/demo-1.0.0.jar` and `build/libs/demo-1.0.0.war` respectively

### Running

`./gradlew apprun`

### Testing

`./gradlew check`