# Keyword Extractor for Resume Building
### Why would I want to use it?
Many companies use ATS to scan resumes and filter applicants, and (according to my advisor) one of the criteria whether the resume has the exact keyword as in the job description. However, job descriptions are long, repeatitive, and extracting keywords from them is tedious. Just like using generative AI tools to rephrase and condense a large paragraph, this tool extracts the keywords to give you a vibe of what could be the focus of your resume.

### Why do I make if from scratch myself?
For fun.

## Instructions
- clone this repo
- copy and paste the job descriptions or additional information to `job_description.txt`
- (optional) play with the paramaters
    - change `focus`, `top` and `ignore` in `extract_keywords.py`
    - to specifically ignore certain words, edit `data/stopwords.txt`
    - edit the `data/keywordlist.txt` if necessary
- run `extract_keywords.py`

### Required package
- nltk

## TODO
- [ ] extract from webpage
- [ ] prettier output

## Sources
- unigram_freq downloaded from [English Word Frequency](https://www.kaggle.com/datasets/rtatman/english-word-frequency)
- demo job_description [Systems Development Engineer Summer Internship – 2025 (US)](https://www.amazon.jobs/en/jobs/2739024/systems-development-engineer-summer-internship-2025-us)