# Projen Python Component

## To use:
- Create a parent folder
  > `mkdir test-repo`
- Make it a git repo
  > `git init`
- Commit the parent repo to GitHub
  > `...`
- Clone this repo into it as a git submodule using GitHub relative path
  > `git submodule add --name projen-python-submodule -b master ../projen-python-submodule projen-python-submodule`
- Run the init script to link the parent repo and the submodule
  > `./projen-python-submodule/projen-init.sh`
- Create a `.projenrc.projdata` file in the parent project, with the options that will be passed to the submodule
  for file generation. `.projenrc.projdata` should look something like the following example:
```
 {
  "name": "p2d-ingress",
  "version": "1.0.0",
  "description": "ROV facing websocket server for accepting P2D messages.",
  "deps": [
    "boto3@^1.17.98",
    "bson@^0.5.10",
    "classutilities@^0.2.1",
    "python@^3.9",
    "requests@^2.26.0",
    "websockets@^10.0"
  ],
  "system_tests": [
    "system_tests/p2d/test_ingress.py",
    "system_tests/p2d/test_p2d.py"
  ]
}
```
- Install projen
  > `nvm install projen`
- Run projen to (re)generate parent project files using parameters from `.projenrc.projdata`
  > `node --inspect .projenrc.js`


## Folder Structure
```
.github
    workflows
      on-push.yml *
skaffold
    python-pod.yml *
src
    __init__.py
    main.py
tests
    __init__.py
    test_example.py
.gitattributes *
.gitignore *
.projenrc.js **
.projenrc.projdata
Dockerfile
README.md
requirements-dev.txt *
requirements.txt *
skaffold.yml
```
\*  Managed by projen

\*\* symlink from projen submodule


## Commands
Notable projen commands

`projen dev` - starts a skaffold dev loop

`projen run` - starts a run-once skaffold

`projen build` - build a docker image

`projen test` - runs pytest
