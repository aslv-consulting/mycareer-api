#!/bin/bash
cd mkdocs
mkdocs build --site-dir ../_site

cd ..
pytest
