version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.9
  pre_build:
    commands:
      - python3.9 -m venv ~/.venv
      - source ~/.venv/bin/activate
      - make install

  build:
    commands:
      - make deploy
