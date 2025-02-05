# mat210-proj-beatties

MAT210 Spring 2021 Final Project - Beatties Ford Road

Deployed with Streamlit at https://share.streamlit.io/wesmith4/mat210-proj-beatties/main/bfr.py.

bit.ly/beatties

## Notes for development

- In "sub-pages" in the `subpages/` directory, be sure to wrap all of your code in an `run()` function after importing necessary modules.
- If you need to import a new module, be sure to do `$ pipreqs --force` in your terminal (in the project directory) to update the `requirements.txt` file.

## Getting Started, Running Streamlit

_Instructions for bash terminal_

1. Clone the repository to your desktop:

```shell
$ git clone https://github.com/wesmith4/mat210-proj-beatties.git
```

2. Install the requirements:

```shell
$ pip install -r requirements.txt
```

3. Start a Streamlit development server:

```shell
$ streamlit run FILE_NAME.py
```

## Streamlit documentation

[Getting Started](https://docs.streamlit.io/en/stable/getting_started.html)

[API Reference](https://docs.streamlit.io/en/stable/api.html) (this will be the most useful)

## Mapping module

A few functions to simplify the process of mapping data onto the maps of NPAs or other geometries have been defined in the `mapping.py` file. To use these functions in your Python script, import this module at the top of the script:

```python
import mapping
```
