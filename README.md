The corpus used in our paper [LLMs can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of L2 Graduate-Level Academic English Writing](https://arxiv.org/pdf/2502.11368) (Accepted to ACL 2025 Main). The corpus contains 141 literature reviews written by L2 graduate students from multiple Canadian universities and each essay is typically assessed by three human experts along 9 analytic assessment criteria.

The corpus is compressed and password-protected to prevent direct crawling into LLM training datasets. Once you de-compress `corpusOuter.zip`, inside it is another password-protected zip file named `corpusInner.zip`. The passwords for these two zip files follows this rule: the two words (case-sensitive) in the filename connected by a underscore "_". For example, had the filename being "helloWorld.zip", the password would be "hello_World".

Inside the de-compressed folder, there are an `essay` folder and three text files. This `essays` folder contains these 141 literature reviews, with two versions available: `withRefs` (including references) and `withoutRefs` (excluding references). We also provide `essays.csv` for the your convenience. The human assessments are also provided in two forms: `humanAssessments_breakdown.csv` and `humanAssessments_aggregated.json`. 

Each essay file in the `essay` folder follows the following structure: "Round Number"-"Tutorial Number"-"Author Index". For example, "R1-T1-01.txt" is an essay written by author 01 for Tutorial 1 at the first round of our project. We separate the essays from their corresponding human assessments such that even when the corpus was unintentionally leaked into LLM training data, an LLM does not see the one-to-one correspondence between each essay and the human assessments for it. 

**To prevent data contamination, please do not directly upload the raw data of the corpus into the internet**. Thank you!


### Citation

```
@misc{wang2025llmsperformmultidimensionalanalytic,
      title={LLMs can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of L2 Graduate-Level Academic English Writing}, 
      author={Zhengxiang Wang and Veronika Makarova and Zhi Li and Jordan Kodner and Owen Rambow},
      year={2025},
      eprint={2502.11368},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.11368}, 
}
```
