# My Career

A restful api for mycareer project

## Development environment

1. Installation

    ```bash
    # Create the development environment
    python3 -m venv .venv
    
    # Activate it
    source .venv/bin/activate

    # Upgrade the package manager
    pip install --upgrade pip

    # Install packages
    pip install -r requirements/dev.txt -r requirements/prod.txt
    ```

2. Run the server

    ```bash
    fastapi dev mycareer/main.py
    ```

    The server is available [here](http://127.0.0.1:8000)

    The api documentation is available [here](http://127.0.0.1:8000/docs)

## Documentation

1. Local documentation

    ```bash
    # Go to documentation folder
    cd mkdocs

    # Generate the documentation
    mkdocs build
    ```

The local project documentation is available [here](_site/index.html)

The github pages is available [here](https://aslv-consulting.github.io/mycareer-api/)

## Tests

```bash
# Run the tests
pytest
```

The test coverage is available [here](reports/coverage/html/index.html)
