# PartsUnlimitedMRP

## Resources

|   |   |
|---|---|
|__GitHub Repository__| https://github.com/SarahBornais/PartsUnlimitedMRP |
|__Pre-Built Files__| [/builds](./builds/) |

## Requirements

Java 8, mongodb

## Introduction

Parts Unlimited MRP is a fictional outsourced Manufacturing Resource Planning (MRP) application for training purposes. It allows users to manage quotes, orders, and deliveries. It also provides a list of fictional dealers and catalog items for purchase.

![image](../images/PartsUnlimitedMRP.png)

The application contains three main components: `IntegrationService`, `OrderService` and `Clients`. The `IntegrationService` integrates the frontend website with the MRP service, the `OrderService` handles customer orders, and the `Clients` component contains the frontend HTML files for application.

### Directory Structure

```
├── builds                                 : contains pre-built JAR and WAR files for the application
├── deploy                                 : instructions and scripts for building and deploying the application
├── labfiles                               : instructions for tutorial labs that use this project as an example
└── src                                    : has the application's source code and test code
    ├── Backend                            : source code and tests for backend services
    │   ├── IntegrationService       
    │   │   ├── build                      : build target directory
    │   │   ├── gradle                     : necessary wrapper files
    │   │   └── src.main    
    │   │       ├── java.integration       : source code for IntegrationService
    │   │       │   ├── infrastructure     : infrastructure configuration
    │   │       │   ├── models             : integration data models
    │   │       │   │   ├── mrp            : internal MRP models
    │   │       │   │   └── website        : models for displaying data on the frontend
    │   │       │   ├── scheduled          : services for periodically updating catalog and order list
    │   │       │   └── services           : main MRP business logic services
    │   │       └── resources              : contains application.properties file
    │   └── OrderService                   : source code and tests for OrderService
    │       ├── build                      : build target directory
    │       ├── buildSrc                   : files to support Microsoft App Insights integration
    │       ├── gradle                     : necessary wrapper files
    │       └── src
    │           ├── main           
    │           │   ├── java.smpl.ordering : source code for OrderService
    │           │   │   ├── controllers    : API endpoint controllers
    │           │   │   ├── models         : order service data models
    │           │   │   └── repositories   : database services
    │           │   │       ├── mock       : classes for mocking database interaction
    │           │   │       └── mongodb    : classes for interacting with MongoDB database
    │           │   │           └── models : data access models  
    │           │   └── resources          : application properties files
    │           └── test                   : JUnit tests for OrderService
    │               ├── java.smpl.ordering
    │               │   ├── controllers    : tests for OrderService controllers
    │               │   └── repositories   : tests for OrderService repository classess
    │               └── resources          : contains application.properties file
    └── Clients                            : source code for frontend services
        ├── build                          : build target directory
        ├── gradle                         : necessary wrapper files
        └── Web                            : frontend HTML, JavaScript, and CSS files
```

## Instructions

First, clone the forked repository:

```
git clone https://github.com/SarahBornais/PartsUnlimitedMRP
cd PartsUnlimitedMRP
```


### Building

We must build three separate services: `OrderService`, `IntegrationService`, and `Clients`.

To build the `OrderService`:

```
cd src/Backend/OrderService
chmod +x gradlew
./gradlew build
```

The JAR file will be created at `src/Backend/OrderService/build/libs/ordering-service-0.1.0.jar`

To build the `IntegrationService`:

```
cd src/Backend/IntegrationService
chmod +x gradlew
./gradlew build
```

The JAR file will be created at `src/Backend/IntegrationService/build/libs//integration-service-0.1.0.jar`

To build the frontend `Clients`:

```
cd src/Clients
chmod +x gradlew
./gradlew build
```

The WAR file will be created at `src/Clients/build/libs/mrp.war`

### Running

Before running the application, we must first set up some data in the MongoDB database.

#### Setting Up the MongoDB Database
1.  Open the mongo command line tools by typing the following command:
    `/usr/bin/mongo`

2.  Select the ordering database to create it.
    `> use ordering`

3. Add an object to the catalog collection

```
> x = {"skuNumber" : "ACC-001", "description" : "Shelving", "unit" : "meters", "unitPrice" : 10.5 }
> db.catalog.insert(x)
```

4.  Check the object was created

    `> db.catalog.find()`

you should see something like:
```
{ "_id" : ObjectId("5568a7aefa7a8f99400cbd1e"), "skuNumber" : "ACC-001", "description" : "Shelving", "unit" : "meters", "unitPrice" : 10.5 }

```

5. Now there is data in the database you can check it with the following command
   `> show dbs`
   Which should show something similar to:
```
local   0.078125GB
ordering        0.203125GB
```

6.  Copy the commands from [MongoRecords.js](https://github.com/SarahBornais/PartsUnlimitedMRP/blob/master/deploy/MongoRecords.js) to insert sample data into the database

#### Running the Services

To run the `OrderService`:

```
cd src/Backend/OrderService/build/libs/
java -jar ordering-service-0.1.0.jar
```

To run the `IntegrationService`:

```
cd src/Backend/IntegrationService/build/libs/
java -jar integration-service-0.1.0.jar
```

The client `mrp.war` file can be run with your preferred method of running WAR files (eg. tomcat, glassfish).

### Testing

`OrderService` is the only one of the three services with Java tests. To run these tests:

```
cd src/Backend/OrderService
./gradlew test
```
