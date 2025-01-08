#!/usr/bin/bash

# Using `uv` as the package manager

uv_dir=$(pwd)/uv
uv_bin=$uv_dir/uv
env_dir=$(pwd)/.venv
env_name=$(basename $(pwd))

function clean()
{
  echo "Cleaning project"
  # Package manager
  [ -d uv/ ] && rm -r uv/ uv.lock
  # Virtual environment
  [ -d .venv/ ] && rm -r .venv/
  # Project dependencies
  [ -f pyproject.toml ] && rm pyproject.toml
  # Builds
  if [ -d dist/ ]
  then
    rm -r dist/
    if [ -d src/ ] && [ -d src/$env_name.egg-info/ ]
    then
      rm -r src/$env_name.egg-info/
    fi
  fi
  if [ ! -z $VIRTUAL_ENV ]
  then
    unset VIRTUAL_ENV
    unset VIRTUAL_ENV_PROMPT
  fi
}

function vcs()
{
  git init
  git config user.name "saptarshi"
  git config user.email "saptarshirajan@gmail.com"

  echo "Creating initial .gitignore"
  touch .gitignore
  echo -e "# Package manager\nuv/\nuv.lock\npyproject.toml\n" >> .gitignore
  echo -e "# Notebooks\n*.ipynb\n" >> .gitignore
}

function main()
{
  while getopts "c" arg
  do
    case "${arg}" in
      c)
        clean
        ;;
      *) echo "Invalid option";;
    esac
    return 0
  done

  # Install uv
  if [ -f $uv_bin ]
  then
    echo "uv is already installed"
  else
    curl -LsSf https://astral.sh/uv/install.sh | \
      env UV_UNMANAGED_INSTALL=$uv_dir sh
  fi

  # Initialize project
  # Remove the hello.py demo file as well (created by uv when initializing)
  $uv_bin init --vcs none --no-pin-python 2>/dev/null \
    && rm hello.py

  # Initialize git repository
  [ ! -d .git/ ] && vcs

  # Create virtual environment
  echo "Creating the virtual environment"
  $uv_bin venv

  # Activate the virtual environment
  if [ ! -z "$VIRTUAL_ENV" ]
  then
    echo "Deactivating previous environment"
    deactivate
  fi
  echo "Activating virtual environment"
  source $env_dir/bin/activate

  #-----------------------------Install packages---------------------------------

  # Packages to be installed (including dependencies):
  # ruff
  # matplotlib
  # scipy
  # jupytext
  # notebook (jupyter, ipykernel, etc)

  $uv_bin add \
    ruff \
    matplotlib \
    scipy \
    jupytext \
    notebook

  # Add environment
  echo "Adding environment to jupyter kernels"
  python -m ipykernel install --prefix=$env_dir --name $env_name
}

main "$@"

