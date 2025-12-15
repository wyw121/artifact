# Case Study Applications 

## Case Study Selection Process

This [excel file](data/paper_case_studies.xlsx) contains the complete list of case study applications used as case studies by at least one of the 24 microservice extraction tools from our tool selection. This resulted in 62 applications. We then looked for case studies with publicly-available Java source code and that have documentation and setup instructions written in English. This resulted in 22 applications, out of which only eight have the corresponding microservice decomposition produced manually by developers. As we intended to use this manually-produced decomposition to facilitate our analysis of results, we further investigated the applicability of these eight applications for our study. 

Specifically, to satisfy the requirements of tools that rely on dynamic analysis, we built each of the applications and executed its corresponding functional test suites. We only included only those applications that have at least 60% statement-level coverage – a
common industrial guideline [11, 14]. To satisfy the requirement of the tools that rely on business use cases for decomposition purposes, we selected case studies with at least three high-level use cases (approximated as functional tests). To satisfy the requirements of the tools that use database relationships for decomposition purposes, we selected case studies with at least three database tables. Finally, to satisfy the requirements of the tool that relies on data from version histories, we selected case studies with at least 100 commits and at least 3 contributors.

This selection resulted in the inclusion of three case study applications: JPetStore, Spring-PetClinic, and PartsUnlimitedMRP. 


To further challenge the tools with new and realistic case studies, in January 2023, we searched for open-source monolithic Java applications in GitHub. We started by identifying the 100 most starred GitHub repositories which contain Java web applications that have at least one commit in the last two years (GitHub Search Query: "web application" OR "web app", language:Java, pushed:>2021-01-
01, archived:False, orderby:stars). 

This [excel file](data/github_case_studies.xlsx) contains the 100 most-starred open-source monolithic Java applications in GitHub that we considered. We then excluded repositories not using English for instructions and documentation, frameworks and tutorials for building web applications, projects that are already implemented as microservices, projects with limited business use cases and test coverage, and projects without databases. We reached out to the owners of the remaining three projects, asking whether they are willing to review and provide feedback on the decompositions of their web apps to microservices produced by automated tools. We received a positive reply from the 7ep-demo owner and included this project in our study. 

In the end, we selected the following four case studies that span multiple application domains:
* JPetStore is an online pet store application;
* Spring-PetClinic is a pet clinic management system;
* PartsUnlimitedMRP is a manufacturing resource planning system;
* 7ep-demo is a web application developed for demonstration purposes.


## Reference Microservice Decomposition of Selected Case Studies

The reference microservice decomposition for each of the case studies can be found in the following links:
* JPetStore: [class-level](data/reference_decomposition/jpetstore_classes.csv), [method-level](data/reference_decomposition/jpetstore_methods.csv)
* Spring-PetClinic: [class-level](data/reference_decomposition/spring-petclinic_classes.csv), [method-level](data/reference_decomposition/spring-petclinic_methods.csv)
* PartsUnlimitedMRP: [class-level](data/reference_decomposition/partsunlimited_classes.csv), [method-level](data/reference_decomposition/partsunlimited_methods.csv)
* 7ep-demo: [class-level](data/reference_decomposition/demo_classes.csv), [method-level](data/reference_decomposition/demo_methods.csv)