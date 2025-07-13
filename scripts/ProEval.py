import re
from llm import get_completion
from prompt_templates import (PROBLEM_EXTRACTION_PROMPT_TEMPLATE, 
                              PROBLEM_CLASSIFICATION_PROMPT_TEMPLATE, 
                              CORRECTION_RELEVANCE_CHECK_PROMPT_TEMPLATE)


def perform_problem_extraction(comment, 
                               model="openai/gpt-4.1-mini-2025-04-14", 
                               temperature=0, max_tries=5):
    prompt = PROBLEM_EXTRACTION_PROMPT_TEMPLATE.substitute(comment=comment)
    return get_completion(prompt, model=model, 
                          temperature=temperature, max_tries=max_tries)


def extract_problems(text):
    if text.strip().lower() == "none":
        return []
    return [p.strip() for p in re.split(r"\n- ", "\n" + text.strip())[1:] if p.strip()]


def perform_problem_classification(excerpt,
                                   model="openai/gpt-4.1-mini-2025-04-14", 
                                   temperature=0, max_tries=5):
     if excerpt.strip().lower() in ["", "none"]:
         return "NO PROBLEM EXISTS"

     prompt = PROBLEM_CLASSIFICATION_PROMPT_TEMPLATE.substitute(excerpt=excerpt)
     return get_completion(prompt, model=model, 
                           temperature=temperature, max_tries=max_tries)


def perform_correction_relevance_check(essay, question, excerpt,
                                       model="openai/gpt-4.1-mini-2025-04-14", 
                                       temperature=0, max_tries=5):
    prompt = CORRECTION_RELEVANCE_CHECK_PROMPT_TEMPLATE.substitute(
        essay=essay, question=question, excerpt=excerpt)
    return get_completion(prompt, model=model, 
                          temperature=temperature, max_tries=max_tries)


def parse_classification_output(llm_output):
    ans = re.findall(r"Yes|No", llm_output)[-3:]
    if len(ans) != 3:
        return "CANNOT_PARSE"
    return ans


def perform_pro_eval(comment, essay=None, question=None,
                     model_for_problem_extraction="openai/gpt-4.1-mini-2025-04-14", 
                     model_for_problem_classification="openai/gpt-4.1-mini-2025-04-14",
                     model_for_correction_relevance_check="openai/gpt-4.1-mini-2025-04-14",
                    temperature=0, max_tries=5):
    output = {"Comment": comment}
    problems = perform_problem_extraction(comment, 
                                          model=model_for_problem_extraction,
                                          temperature=temperature, 
                                          max_tries=max_tries)
    
    for i, problem in enumerate(extract_problems(problems)):
        output[f"Problem_{i+1}"] = problem
        problem_clfs = perform_problem_classification(problem, 
                                                      model=model_for_problem_classification,
                                                      temperature=temperature, 
                                                      max_tries=max_tries)
        problem_clfs_parsed = parse_classification_output(problem_clfs)
        output["Problem Classification"] = {"LLM Output": problem_clfs, 
                                            "Parsed Output": problem_clfs_parsed}
        
        if problem_clfs_parsed and problem_clfs_parsed[-1] == "Yes":
            if essay is not None and question is not None:
                correction_relevance_check = perform_correction_relevance_check(
                    essay, question, problem, model=model_for_correction_relevance_check,
                    temperature=temperature, max_tries=max_tries)
                correction_relevance_check_parsed = parse_classification_output(
                    correction_relevance_check)
                output["Correction Relevance Check"] = {
                    "LLM Output": correction_relevance_check,
                    "Parsed Output": correction_relevance_check_parsed
                }
            else:
                output["Correction Relevance Check"] = {
                    "LLM Output": "",
                    "Parsed Output": ""
                }
    return output