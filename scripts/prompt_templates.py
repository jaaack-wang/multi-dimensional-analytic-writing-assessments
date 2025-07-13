from string import Template


PROBLEM_EXTRACTION_PROMPT_TEMPLATE = '''
You will be given a feedback comment written for a student's essay. Your task is to \
identify and extract all the writing-related problems mentioned or implied in the comment, along with any \
explanations, suggestions, corrections, questions, quotations, or other relevant information provided \
in the comment for each extracted problem. 

A writing-related problem is any issue that affects the quality of the writing, such as citation errors, \
logical flaws, coherence issues, grammatical mistakes, or inappropriate word choices, among others. 

### Extraction Instructions

- Each extracted problem must be clear and can be understood without the need to refer to the original comment. 

- Each extracted problem must faithfully reflect the provided comment by including any relevant information. Relevant information \
includes a further explanation or an elaboration of the problem, a suggestion for improvement, a concrete correction, a clarifying question, \
an excerpt (possibly without quotation marks) from the student's essay, or any other relevant information that helps to understand the problem. 

- Whenever possible, extract each problem and the relevant information as they are written in the comment.

### Output Instructions

- Output each extracted problem along with their relevant information line by line headed by "-".
- Output "None" if no writing-related problems are mentioned or implied in the comment.

### Examples

Example 1 input:

The content is generally informative and relevant, but the clarity of ideas could be improved. Some sentences are overly complex and could be simplified for better understanding. For instance, the sentence "Gandhi's Satyagraha as an adequate substitute for violent methods of conducting social conflict in an early and thorough philosophical examination of Gandhi's attitude to violence in extreme group conflict" is difficult to parse and could be rephrased for clarity.

Example 1 output:

- The clarity of ideas could be improved. Some sentences are overly complex and could be simplified for better understanding. For instance, the sentence "Gandhi's Satyagraha as an adequate substitute for violent methods of conducting social conflict in an early and thorough philosophical examination of Gandhi's attitude to violence in extreme group conflict" is difficult to parse and could be rephrased for clarity.

Example 2 input:

The content and clarity of ideas are generally good, but there are some areas where the author could provide more depth or analysis. For example, the author could have explored the potential reasons why students in India may be more vulnerable to substance abuse, or discussed the implications of legalization for public health policy. To improve, the author could revisit the body of the literature review and provide more nuanced analysis of the findings.

Example 2 output:

- There are some areas where the author could provide more depth or analysis. For example, the author could have explored the potential reasons why students in India may be more vulnerable to substance abuse, or discussed the implications of legalization for public health policy. To improve, the author could revisit the body of the literature review and provide more nuanced analysis of the findings.

Example 3 input:

The author has generally done a good job of integrating source materials and presenting information clearly. However, there are some instances where the connections between ideas could be more explicitly stated, and the citation practices could be more consistent (e.g., some sources are cited with author names, while others are cited with only the year).

Example 3 output:

- There are some instances where the connections between ideas could be more explicitly stated.
- The citation practices could be more consistent (e.g., some sources are cited with author names, while others are cited with only the year).

### Input

$comment

### Output
'''.strip()


PROBLEM_CLASSIFICATION_PROMPT_TEMPLATE = '''
You will be given an excerpt of a feedback comment written for a student's essay. Your task is to answer the following questions:

1. Does the excerpt refer to a specific part of the essay? A specific part refers to a part of the essay that can be easily located by the student. \
For example, it can be a specific word, phrase, sentence, paragraph, reference etc. used in the essay. It can be a concrete location, such as \
"sentence 2 in paragraph 2," "in paragraph 6," "the first citation," or "the first sentence of the paper" and so on. A less concrete location, such as \
"the introduction," or "the conclusion," is also considered a specific part if it is accompanied by some referencable details, such as \
"The significance of South Australian policy is unclear, as it is the first citation and the only one in the Introduction." Note that the excerpt \
may only contain a quoted text from the essay, in which case, the quoted text is considered a specific part.

2. Does the excerpt offer some form of suggestions, general or specific, for the student to improve the essay? If the excerpt only describes a problem \
and it is unclear what the student should do to fix it, then there is no suggestion. If the excerpt provides a concrete correction, it is considered a suggestion.

3. Does the excerpt provide a concrete correction for the student to apply? Note that when the excerpt only contains a quoted text from the essay and there \
are some notes indicating a correction (e.g., adding/removing a punctuation, correcting a spelling), this is considered a correction.

Answer each question with "Yes" or "No" based on the content of the excerpt and briefly justify your answer. After answering all the questions, \
produce your final answers in a newline separated by commas.

Excerpt: $excerpt
'''.strip()


CORRECTION_RELEVANCE_CHECK_PROMPT_TEMPLATE = '''
You will be given an excerpt of a feedback comment written for a student's essay according to an assessment question. Your task is to answer the following questions: 

1. Does the problem pointed out in the excerpt exist in the corresponding essay? If the excerpt uses a quoted text to point out a problem, check if the quoted text is present in the essay. \
Please note that the quoted text may not be an exact match either due to misspellings, capitalization errors etc., or because the quoted already contains the correction in place. 

2. Is the problem pointed out in the excerpt relevant to the corresponding assessment question? Check if the excerpt is broadly related to any aspect of the assessment question. 

3. Is the correction of the problem pointed out in the excerpt correct? If the problem does exist in the essay, check if the correction fixes the problem or presents a plausible solution or improvement.

Here is the essay:

$essay

Here is the assessment question:

$question

Here is the excerpt:

$excerpt

Answer each question with "Yes" or "No" utilizing all the information provided and briefly justify your answer. After answering all the questions, produce your final answers in a newline separated by commas.
'''.strip()


PROBLEM_EXTRACTION_PROMPT_TEMPLATE = Template(PROBLEM_EXTRACTION_PROMPT_TEMPLATE)
PROBLEM_CLASSIFICATION_PROMPT_TEMPLATE = Template(PROBLEM_CLASSIFICATION_PROMPT_TEMPLATE)
CORRECTION_RELEVANCE_CHECK_PROMPT_TEMPLATE = Template(CORRECTION_RELEVANCE_CHECK_PROMPT_TEMPLATE)