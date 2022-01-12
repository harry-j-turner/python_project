#!/bin/bash

# Run Flake8
echo -e "\nLinting..."
poetry run flake8 src/
echo -e "Done."

# Run MyPy
echo -e "\nType Check..."
echo "It is recommended you use a virtual environment to install any recommended mypy packages."
python3.9 -m mypy src/
echo -e "Done."
