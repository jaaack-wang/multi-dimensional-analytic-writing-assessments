## Description

This repo is for our paper titled [LLMs can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of L2 Graduate-Level Academic English Writing](https://arxiv.org/pdf/2502.11368) (Accepted to ACL 2025 Main). It contains (1) a previously unpulished corpus of 141 graudate-level L2 literature reviews annotated with multi-dimensional analytic writing assessments ; (2) and the code for the feedback comment quality evaluation framework `ProEval` we propose and validate in the paper.



## Data

The corpus contains 141 literature reviews written by L2 graduate students from multiple Canadian universities and each essay is typically assessed by three human experts along 9 analytic assessment criteria.

The corpus is compressed and password-protected to prevent direct crawling into LLM training datasets. Once you de-compress `corpusOuter.zip`, inside it is another password-protected zip file named `corpusInner.zip`. The passwords for these two zip files follows this rule: the two words (case-sensitive) in the filename connected by a underscore "_". For example, had the filename being "helloWorld.zip", the password would be "hello_World".

Inside the de-compressed folder, there are an `essay` folder and three text files. This `essays` folder contains these 141 literature reviews, with two versions available: `withRefs` (including references) and `withoutRefs` (excluding references). We also provide `essays.csv` for the your convenience. The human assessments are also provided in two forms: `humanAssessments_breakdown.csv` and `humanAssessments_aggregated.json`. 

Each essay file in the `essay` folder follows the following structure: "Round Number"-"Tutorial Number"-"Author Index". For example, "R1-T1-01.txt" is an essay written by author 01 for Tutorial 1 at the first round of our project. We separate the essays from their corresponding human assessments such that even when the corpus was unintentionally leaked into LLM training data, an LLM does not see the one-to-one correspondence between each essay and the human assessments for it. 

**To prevent data contamination, please do not directly upload the raw data of the corpus into the internet**. Thank you!



## ProEval

The open-source the full base code for `ProEval` in the `scripts` folder. Below is an example use:

```python
from ProEval import perform_pro_eval

comment = '''The author has generally done a good job of integrating the source materials into the text, with clear summaries and explanations of the findings. However, there are some areas where the citation practices could be improved. For example, some of the in-text citations are not formatted correctly (e.g., "Wilkinson ST, etal., 2015" should be "Wilkinson et al., 2015"), and there are some inconsistencies in the reference list (e.g., some sources have DOIs, while others do not). Additionally, the author could benefit from using more precise language when describing the findings of the studies, rather than relying on general statements.'''

output = perform_pro_eval(comment)
```



By default, the tool uses `gpt-4.1-mini-2025-04-14` with a 0 temperature. The output we obtained is as follows:

```
{
    "Comment": "...(Left out to reduce spaces)",
    "Problem_1": "Some of the in-text citations are not formatted correctly (e.g., \"Wilkinson ST, etal., 2015\" should be \"Wilkinson et al., 2015\").",
    "Problem Classification": {
        "LLM Output": "1. No - The excerpt does not refer to a specific part of the essay; it only gives a general comment about the language used to describe findings without pointing to a particular sentence, paragraph, or phrase.  \n2. Yes - The excerpt suggests that the author should use more precise language instead of general statements, which is a form of advice for improvement.  \n3. No - The excerpt does not provide a concrete correction or example of how to make the language more precise; it only offers a general suggestion.  \n\nNo, Yes, No",
        "Parsed Output": [
            "No",
            "Yes",
            "No"
        ]
    },
    "Correction Relevance Check": {
        "LLM Output": "",
        "Parsed Output": ""
    },
    "Problem_2": "There are inconsistencies in the reference list (e.g., some sources have DOIs, while others do not).",
    "Problem_3": "The author could benefit from using more precise language when describing the findings of the studies, rather than relying on general statements."
}
```



In the paper, we used `gpt-4o-2024-11-20` for both Problem Extraction and Problem Classification and `gpt-4-turbo-2024-04-09` for Correction Relevance Check. Argubaly, more advanced models should not underperform these two models. By default, `perform_pro_eval`  performs Problem Extraction and Problem Classification. To enable Correction Relevance Check, we need to provide the original essay and the question for which the provided comment was written.

We use [litellm](https://github.com/BerriAI/litellm) to call LLMs, so please follow the model calling instruction to use it (provider + LLM model name).



## Citation

```
@inproceedings{wang-etal-2025-llms-perform,
    title = "{LLM}s can Perform Multi-Dimensional Analytic Writing Assessments: A Case Study of {L}2 Graduate-Level Academic {E}nglish Writing",
    author = "Wang, Zhengxiang  and
      Makarova, Veronika  and
      Li, Zhi  and
      Kodner, Jordan  and
      Rambow, Owen",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.423/",
    doi = "10.18653/v1/2025.acl-long.423",
    pages = "8637--8663",
    ISBN = "979-8-89176-251-0",
}
```

Also consider citing the related papers based on the corpus.

```
@article{li2023developing,
  title={Developing literature review writing and citation practices through an online writing tutorial series: Corpus-based evidence},
  author={Li, Zhi and Makarova, Veronika and Wang, Zhengxiang},
  journal={Frontiers in Communication},
  volume={8},
  pages={1035394},
  year={2023},
  publisher={Frontiers Media SA}
}
```

```
@inproceedings{li2023assessment,
  title={Assessment of academic esl writing in an online tutorial for graduate students},
  author={Li, Zhi and Makarova, Veronika and Wang, Zhengxiang},
  year={2023}
}
```

