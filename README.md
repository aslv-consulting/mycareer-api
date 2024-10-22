# My Career API

A REST API for the My Career project.

## Development Environment

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade the package installer
pip install --upgrade pip

# Install the packages
pip install -r requirements/dev.txt -r requirements/prod.txt

# Start the server
fastapi dev mycareer/main.py
```

The api is available [here](http://localhost:8000)

The API documentation is available [here](http://localhost:8000/docs)

## Tests

```bash
# Run test
pytest
```

The html coverage is available [here](reports/coverage/index.html)

## Changlog

The changelog is available [here](CHANGELOG.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
