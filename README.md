# Setup instructions
Work in progress
```
conda create --name planner python=3.11
```
```
conda activate planner
```
```
pip3 install -r requirements.txt
```
```
conda deactivate
```
```
 python3 ./planner.py  -h
```

# The idea
- remove the complexity of creating very well defined prompts for a specific task (re-use of carefully crafted prompts)
- in systems_prompts we need to development very well generic crafted description of how to plan things <br>
    (ex. software developent, training creation, etc ...)
- in tasks, we define what plan to develop (ex create a pdf analyzer)
- the result is a detailed plan that can be used by for ex. in ChatGPT o1-preview to develop the idea

