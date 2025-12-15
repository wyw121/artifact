# Guidelines to Tool Authors


## Introduction

This repository contains the case study package for comparison of microservice decomposition tools. 

When selecting the case studies, we aimed to ensure that each case study can be processed by each of the tools participating in our study. Specifically, all selected projects are in Java and do not use any framework other than Spring. We made sure to build, run, and trigger tests for all the case studies and selected those with a relatively high test coverage. 

At the end of the process, we selected four case studies (listed in the table below), which include three monolithic applications used in prior literature and an additional monolithic application that was not used in prior work.

The selected case studies are listed in the table below:

| Case Study                                         | Instructions | GitHub Forked Repository | Framework | Number of Classes | Test Coverage |
| :-------------------------------------------------- | - | ----------- | --------- | ----------------- | ------------- | 
| JPetStore   |  [Instructions](data/jpetstore/README.md) | [link](https://github.com/SarahBornais/jpetstore-6)   | Spring    | 24                | 64%           | 
| spring-petclinic   | [Instructions](data/spring-petclinic/README.md)  | [link](https://github.com/SarahBornais/spring-petclinic)  | Spring    | 23                | 94%           | 
| PartsUnlimitedMRP |  [Instructions](data/partsunlimitedmrp/README.md) | [link](https://github.com/SarahBornais/PartsUnlimitedMRP)  | Spring    | 53               | 65%           | 
| 7ep-demo    |   [Instructions](data/7ep-demo/README.md)  | [link](https://github.com/SarahBornais/demo)  | None      | 47                | 93%           |


The Instructions column in the table above contains a link to a directory we created, which includes instructions on how to build, run, and test the corresponding case study. We forked a particular version of each case study GitHub repository to ensure all tools use the same version in their decomposition. The GitHub Forked Repository column in the table above, as well as each case study Instructions directory, contains a link to this forked version. 

## Step 1. Building, Running, and Testing the Case Studies

Depending on the needs of the microservice decomposition tool, it may be necessary to build, run, and/or test each of the case study applications. Instructions on how to do so are located in the `README` file under each of the case studies' Instructions directories.

The Instructions’ `/builds` directory contains pre-built JAR and/or WAR files, depending on the type of application. These build files can be used as an input to the decomposition tools. 

If a tool requires additional input formats (e.g., instrumentation or similar), custom inputs can be created using the building, running, and testing instructions, as described in each case study Instructions directory. __Note: please use forked repository linked in the table above to perform any of these tasks.__

## Step 2. Reporting results

Please report the tool partitioning result in the standard JSON format specified below. We have provided a template JSON output file, named `reporting-template.json`, pre-populated with the names of the classes of a case study, in its corresponding Instructions directory. These templates place all the classes of the given case study into a single partition, representing the current monolithic state of the case studies.

An example of the JSON structure is provided below. The first key, `my_tool` is the name of the tool that created the decomposition. In this example, the decomposition contains 2 partitions: `partition0`, and `partition1`. If a decomposition contains more than 2 partitions, additional keys such as `partition2`, `partition3`, etc., can be added. Each of the partition JSON objects contains an array of JSON objects representing the classes contained in the decomposition. Each of these class objects has only a single property, `id`, whose value is the name of the class it represents.

```json
{
  "my_tool": {
    "decomposition": {
      "partition0": [
        {
          "id": "ClassA"
        },
        {
          "id": "ClassB"
        }
      ],
      "partition1": [
        {
          "id": "ClassC"
        },
        {
          "id": "ClassD"
        }
      ]
    }
  }
}
```
