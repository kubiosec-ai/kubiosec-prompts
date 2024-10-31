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
- in systems_prompts we need to development very well generic crafted description of how to plan things (ex. software developent, training creation, etc ...)
- in tasks, we define what plan to develop (ex create a pdf analyzer)
- the results is detailed plan that can be used by for ex GPT-4oi to develop the idea

