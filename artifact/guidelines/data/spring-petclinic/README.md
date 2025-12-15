# spring-petclinic

## Resources

|   |   |
|---|---|
|__GitHub Repository__| https://github.com/SarahBornais/spring-petclinic |
|__Pre-Built Files__| [/builds](./builds/) |

## Requirements

Java version 17 or greater

## Introduction

The spring-petclinic application is a demo application that enables the management of a pet clinic's veternarians, clients, pets, and visits. A user can add and modify clients, pets, and visits through a simple web interface.

![image](../images/spring-petclinic.png)

### Directory Structure

```
├── .mvn                         : necessary maven wrapper files
├── gradle                       : necessary gradle wrapper files
└── src                          : has the application's source code and all test code
    ├── checkstyle               : code style checker settings
    ├── main                     : source code for the application
    │   ├── java    
    │   │   ├── model            : data models for the application  
    │   │   ├── owner            : services to manage owners, pets, and visits
    │   │   ├── system           : infrastructure services
    │   │   └── vet              : services to manage vets
    │   ├── resources            : non-Java files
    │   │   ├── db               : sql files to create and populate databases
    │   │   │   ├── h2    
    │   │   │   ├── hsqldb  
    │   │   │   ├── mysql  
    │   │   │   └── postgress  
    │   │   ├── messages         : configuration files for messages displayed to user
    │   │   ├── static.resources : fonts and image resources for displaying the frontend
    │   │   └── templates        : html templates to display on the frontend
    │   └── scss                 : frontend stylesheets
    └── test                     : tests that target the UI
        ├── java                 : unit and integration tests for the application
        └── jmeter               : test plan to use with JMeter
```

## Instructions

First, clone the forked repository:

```
git clone https://github.com/SarahBornais/spring-petclinic
cd spring-petclinic
```

### Building

Run `./mvnw package`

The JAR file will be created at `target/spring-petclinic-3.0.0-SNAPSHOT.jar`

### Running

Run either `java -jar target/*.jar` or `./mvnw spring-boot:run`

### Testing

Run `./mvnw test`