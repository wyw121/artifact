# Tools

## Microservice extraction technique identification

To identify additional proposing microservice decomposition techniques published from 2022 to January 2024, we performed a systematic search following the methodology used by [Abgaz et al.](https://ieeexplore.ieee.org/document/10160171/).

Search query: 

* Query = Monolith AND Microservice AND Decomposition
* Monolith = monolith* OR exist* OR legacy
* Microservice = microservice* OR micro-service*
* Decomposition = decompos* OR migrat* OR identif* OR extract* OR refactor* OR modular* OR transform* OR transit* OR conver*

Databases: 
* SpringerLink 
* IEEE Xplore 
* ACM Digital Library 
* Science Direct 
* Wiley Online
* Scopus


Inclusion criteria:
* (IC1) the primary objective of the study should be the decomposition of monolithic applications into microservices,
* (IC2) the study should include structured and preferably automatic or semi-automated decomposition approaches,
* (IC3) the study should sufficiently describe the decomposition method, code, algorithm, and its evaluation.

Exclusion criteria. In addition exclusion criteria applied by Abgaz et al. (EC1-EC5), we also exclude publications from non-A*/A venues according to the CORE ranking (EC6) or techniques that rely on additional artifacts that are often unavailable or requiring a considerable time to produce (EC7), e.g., entity-relationship and use case diagrams, as was also done in prior work:
* (EC1) duplicate study 
* (EC2) books and patents 
* (EC3) non-peer-reviewed study
* (EC4) secondary studies 
* (EC5) study written in a language other than English
* (EC6) papers from non-A*/A venues 
* (EC7) papers that rely on additional artifacts that are often unavailable or require a considerable time to produce

We also conducted a forward and backward snowballing search on the papers identified in the initial search, as in Abgaz et al. 
The snowballing process does not result in any additional qualified papers. 

In the end, together with techniques collected by Abgaz et al., we identified a total of 24 publications that satisfy all selection criteria. 
We thus consider these 24 publications for our study. 

This [excel file](data/tools.xlsx) contains data on our search and analysis of the papers. 
The first two tabs of the file contain the list of papers (from Abgaz et al., and returned from our query) and our analysis of the papers applying inclusion and exclusion criteria. 


## Tool authors invitation and their reply

We reached out to all authors of all 24 identified publications and sent an additional reminder two weeks after the initial contact, in case we did not receive a reply by then.

We received positive replies from authors of ten publications, who agreed to participate in our study. 
In two cases, different publications came from the same group and involved different versions of the same tool. We gave these authors the freedom to run their desired version of their respective tools.
All but one participating tool worked for Java applications. Thus, to enable meaningful comparison, we had to exclude the single tool that works for Python.

Finally, to make sure we cover all microservice decomposition principles (Goal 1), we decided to include the single tool that relies on code evolution (and optimizes for team independence) when decomposing to microservices, which we ran ourselves.

The table below lists the 24 tools and marks ones that we received a positive confirmation from the authors. The same data can also be found in the third tab of the same [excel file](data/tools.xlsx) from the previous section.

| Paper Title | Authors | Year | Venue | Agree to Participate |
|---|---|---|---|---|
| Extraction of Microservices from Monolithic Software Architectures | Genc Mazlami, Jürgen Cito, Philipp Leitner | 2017 | ICWS | * we run ourselves |
| Tool Support for the Migration to Microservice Architecture: An Industrial Case Study | Ilaria Pigazzini, Francesca Arcelli Fontana, Andrea Maggioni  | 2019 | ECSA |  |
| From a Monolith to a Microservices Architecture: An Approach Based on Transactional Contexts | Luís Nunes, Nuno Santos, António Rito Silva | 2019 | ECSA |  |
| Unsupervised learning approach for web application auto-decomposition into microservices | Muhammad Abdullah, Waheed Iqbal, Abdelkarim Erradi | 2019 | JSS |  |
| Service Candidate Identification from Monolithic Systems based on Execution Traces | Wuxia Jin, Ting Liu, Yuanfang Cai, Rick Kazman, Ran Mo, Qinghua Zheng | 2019 | TSE |  |
| From Monolithic Architecture Style to Microservice one Based on a Semi-Automatic Approach | Anfel Selmadji, Abdelhak-Djamel Seriai, Hinde Lilia Bouziane, Rahina Oumarou Mahamane, Pascal Zaragoza, Christophe Dony | 2020 | ICSA |  |
| Remodularization Analysis for Microservice Discovery Using Syntactic and Semantic Clustering | Adambarage Anuruddha Chathuranga De Alwis, Alistair Barros, Colin Fidge, Artem Polyvyanyy  | 2020 | CaiSE |  |
| Automated Microservice Identification in Legacy Systems with Functional and Non-Functional Metrics | Yukun Zhang, Bo Liu, Liyun Dai, Kang Chen, Xuelian Cao | 2020 | ICSA | Yes, multiple publications from the same group |
| Determining Microservice Boundaries: A Case Study Using Static and Dynamic Software Analysis | Tiago Matias, Filipe F. Correia, Jonas Fritzsch, Justus Bogner, Hugo S. Ferreira, André Restivo  | 2020 | ECSA | Yes, later excluded for not supporting Java |
| Monolith to Microservice Candidates using Business Functionality Inference | Shivali Agarwal, Raunak Sinha, Giriprasad Sridhara, Pratap Das, Utkarsh Desai, Srikanth Tamilselvam, Amith Singhee, Hiroaki Nakamuro | 2021 | ICWS |  |
| Graph Neural Network to Dilute Outliers for Refactoring Monolith Application | Utkarsh Desai, Sambaran Bandyopadhyay, Srikanth Tamilselvam | 2021 | AAAI |  |
| Microservice Remodularisation of Monolithic Enterprise Systems for Embedding in Industrial IoT Networks | Adambarage Anuruddha Chathuranga De Alwis, Alistair Barros, Colin Fidge, Artem Polyvyanyy  | 2021 | CaiSE |  |
| A Multi-Criteria Strategy for Redesigning Legacy Features as Microservices: An Industrial Case Study | Wesley K. G. Assunção, Thelma Elita Colanzi, Luiz Carvalho, Juliana Alves Pereira, Alessandro Garcia, Maria Julia de Lima, Carlos Lucena | 2021 | SANER | Yes |
| Mono2Micro: A Practical and Effective Tool for Decomposing Monolithic Java Applications to Microservices | Anup K. Kalia, Jin Xiao, Rahul Krishna, Saurabh Sinha, Maja Vukovic, Debasish Banerjee | 2021 | FSE | Yes |
| A Hierarchical DBSCAN Method for Extracting Microservices from Monolithic Applications | Khaled Sellami, Mohamed Aymen Saied, Ali Ouni | 2022 | EASE | Yes, multiple publications from the same group |
| CARGO: AI-Guided Dependency Analysis for Migrating Monolithic Applications to Microservices Architecture | Vikram Nitin, Shubhi Asthana, Baishakhi Ray, Rahul Krishna | 2022 | ASE | Yes |
| Combining Static and Dynamic Analysis to Decompose Monolithic Application into Microservices | Khaled Sellami, Mohamed Aymen Saied, Ali Ouni, Rabe Abdalkareem | 2022 | ICSOC | Yes, multiple publications from the same group |
| Improving microservices extraction using evolutionary search | Khaled Sellami, Ali Ouni,  Mohamed Aymen Saied, Salah Bouktif, Mohamed Wiem Mkaouer | 2022 | Info. Soft. Tech. | Yes, multiple publications from the same group |
| Leveraging the Layered Architecture for Microservice Recovery | Pascal Zaragoza, Abdelhak-Djamel Seriai, Abderrahmane Seriai, Anas Shatnawi, Mustapha Derras | 2022 | ICSA |  |
| Log2MS: a framework for automated refactoring monolith into microservices using execution logs | Bo Liu, Jingliu Xiong, Qiurong Ren, Shmuel Tyszberowicz, Zheng Yang | 2022 | ICWS | Yes, multiple publications from the same group |
| Monolith to Microservices: Representing Application Software through Heterogeneous Graph Neural Network | Alex Mathai, Sambaran Bandyopadhyay, Utkarsh Desai, Srikanth Tamilselvam | 2022 | IJCAI |  |
| Towards Migrating Legacy Software Systems to Microservice-based Architectures: a Data-Centric Process for Microservice Identification | Yamina Romani, Okba Tibermacine, Chouki Tibermacine | 2022 | ICSA-C | Yes |
| Microservice extraction using graph deep clustering based on dual view fusion | Lifeng Qian, Jing Li, Xudong He, Rongbin Gu, Jiawei Shao, Yuqi Lu | 2023 | Info. Soft. Tech. |  |
| From monolithic to microservice architecture: an automated approach based on graph clustering and combinatorial optimization | Gianluca Filippone, Nadeem Qaisar Mehmood, Marco Autili, Fabrizio Rossi, Massimo Tivoli | 2023 | ICSA | Yes |
