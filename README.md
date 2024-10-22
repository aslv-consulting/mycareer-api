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

## Migration

```bash
# Create a migration
alembic revision --autogenerate -m"message"

# Migrate
alembic upgrade head

# Downgrade the last commit
alembic downgrade -1

# Downgrade until the commit
alembic downgrade <revision>

# Reset the database
alembic downgrade base
```

## Tests

```bash
pytest
```

The html coverage is available [here](reports/coverage/index.html)

## Linter

```bash
pylint mycareer tests
```

## Changlog

The changelog is available [here](CHANGELOG.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
