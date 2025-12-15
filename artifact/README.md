# Microservice Decomposition Techniques: An Independent Tool Comparison

## Overview 

The microservice-based architecture -- a SOA-inspired principle of dividing systems into components that communicate with each other using language-agnostic APIs -- has gained increased popularity in industry. Yet, migrating a monolithic application into microservices is a challenging task. A number of automated microservice decomposition techniques have been proposed in industry and academia to help developers with the migration complexity. Each of the techniques is usually evaluated on its own set of case study applications and evaluation criteria, making it difficult to compare the techniques to each other and assess the real progress in this field. 
To fill this gap, this paper performs an independent study comparing six microservice decomposition tools that implement a wide range of different decomposition principles with each other on a set of four carefully selected benchmark applications. The results of our analysis highlight strengths and weaknesses of existing approaches and propose suggestions for future research. 

In this artifact, we provide the data collected/generated and scripts implemented in our paper. 

## Paper Information

You can find the submitted version of our paper [here](https://tinyurl.com/3y9p279w). 

If you use this artifact or part of it, please cite our paper

```
@inproceedings{Wang:Bornais:Rubin:ASE:2024,
  title={{Microservice Decomposition Techniques: An Independent Tool Comparison}},
  author={Wang, Yingying and Bornais, Sahar and Rubin, Julia},
  booktitle={Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE'24),}
  year={2024}
}
```

## Artifact Structure

We organize the data and scripts by folders: 
* [Tools](#tools)
* [Case Studies](#case-studies)
* [Guidelines](#guidelines)
* [Metrics](#metrics)
* [Results](#results)

In each folder, besides the data and scripts (if any), we also provide a document explaining how the data is collected and organized and how to run the scripts when applicable.

### Tools 
[documentation](tools/README.md), [data](tools/data)

Here we share
* our microservice extraction technique identification process and results
* tools we sent invitation to participate in our study and the reply from tool authors

### Case Studies
[documentation](case_studies/readme.md), [data](case_studies/data)

Here we share 
* our case study application selection process and results
* identified reference decompositions of the selected case study applications


### Guidelines 
[documentation](guidelines/readme.md), [data](guidelines/data)

Here we share 
* the guidelines we sent to all participating tool authors on how to build, run, test the case studies as well as the desired format of our output 

### Metrics
[documentation](metrics/readme.md), [scripts](metrics/scripts)

Here we share 
* our metric selection process
* the script we implemented to calculate decomposition metric results

### Results

[documentation](results/readme.md), [data](results/data)

Here we share 
* participating tools' raw results
* our quantitative evaluation results
* our qualitative evaluation results

## License 

The data and documentation of this artifact is licensed under the [Creative Commons Attribution 4.0 International license](https://choosealicense.com/licenses/cc-by-4.0/), and the scripts we share is licensed under the [MIT license](https://github.com/github/choosealicense.com/blob/gh-pages/LICENSE).

## Contact 

For questions about our paper or artifact, please contact Yingying Wang (wyingying@ece.ubc.ca).