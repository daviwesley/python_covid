## Instalation

Run the following to install

```python
pip install python-covid
```

## Usage

```python
from python_covid.client import Client

## get all recents cases
cases = Client()
```
## Setting up enviroment for development
- Make sure you have pip installed
- Install the python package `pipenv` with `pip install pipenv`

Run the following commands to set up your local enviroment
```
pipenv shell
```
```
pipenv install && pipenv install --dev
```

## Documentation
[docs](https://daviwesley.github.io/python_covid/)

use the following command to see a webpage with the documentation
```bash
$ mkdocs serve
```
