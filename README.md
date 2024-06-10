## Developments

- Create a new venv
``` zsh
## Navigate to you project directory
## Create a new venv if it doesn't exist
python3 -m venv venv 
```


- Activate venv
``` zsh
## Activate venv
source venv/bin/activate

## Validate Python interpreter version
python --version
```

- Download dependencies
``` zsh
## Navigate to path containing "setup.py"
pip install -e .
```

- Run unit tests
``` zsh
## Navigate to path containing "setup.py"
pytest
```



