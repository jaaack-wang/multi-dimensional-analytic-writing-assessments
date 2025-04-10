The corpus used in our paper [LLMs can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of L2 Graduate-Level Academic English Writing](https://arxiv.org/pdf/2502.11368). The corpus contains 141 literature reviews written by L2 graduate students from multiple Canadian universities and each essay is typically assessed by three human experts along 9 analytic assessment criteria.

The corpus is compressed and password-protected to prevent direct crawling into LLM training datasets. The password for the compressed zip file `corpus.zip` is `corpus`. Once you de-compress it, you will find another zip file named  `corpus.file`, but without password protection. The reason for having two layers of compression again is to prevent direct crawling. 

Inside the de-compressed folder, there are an `essay` folder and two text files. This `essays` folder contains these 141 literature reviews, with two versions available: `withRefs` (including references) and `withoutRefs` (excluding references). The human assessments are also provided in two forms: `humanAssessments_breakdown.csv` and `humanAssessments_aggregated.json`.

To prevent data contamination, please do not directly upload the raw data of the corpus into the internet! 


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
