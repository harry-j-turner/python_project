const fs = require("fs");
const path = require("path");
const {
  CustomPythonProject,
} = require("./.projenrc.types/custom-python-project");
const options = JSON.parse(
  fs.readFileSync(path.join(__dirname, "..", ".projenrc.projdata")).toString()
);

const customPythonProject = new CustomPythonProject({
  authorEmail: "rob.fisher@vaarst.com",
  authorName: "Vaarst",
  moduleName: options.name.replace(/[-]/g, "_") /* create 'slug' from name */,
  name: options.name,
  version: options.version ?? "0.1.0",
  deps: options.deps /* List of runtime dependencies for this project. */,
  description: options.description /* A short description of the package. */,
  defaultDockerPort:
    options.defaultDockerPort /* A single pod is created by default, you can specify the port to expost here. */,
  devDeps: [

    /* Formatting dependencies. */
    "black@21.12b0" /* The opinionated code formatter. */,

    /* Testing Dependencies */
    "coverage@6.2" /* For reporting test coverage. */,
    "moto@2.2.17" /* For mocking AWS calls. */,
    "nox@2022.1.7" /* For testing against multiple Python environments */,
    "pytest@6.2.5" /* Python test runner. */,
    "pytest-mock@3.6.1" /* For mocking function calls. */,
    "pytest-asyncio@0.16.0" /* For mocking asynchronous function calls. */,
    "pytest-cov@3.0.0" /* For reporting test coverage. */,
    "requests-mock@1.9.3" /* For mocking network requests. */,

    /* Linting Dependencies */
    "darglint@1.8.1" /* Ensure docstrings stay in sync with source code. */,
    "flake8@4.0.1" /* Base linter. */,
    "flake8-annotations" /* For checking type annotations. */,
    "flake8-bandit@2.1.2" /* For checking safety issues. */,
    "flake8-black@0.2.3" /* For checking for formatting issues. */,
    "flake8-bugbear@21.11.29" /* For checking for common bugs. */,
    "flake8-docstrings@1.6.0" /* For checking docstrings. */,
    "flake8-import-order@0.18.1" /* For checking for import order. */,

    /* Typing Dependencies */
    "mypy@0.931" /* Static type checking. */,
    "types-requests@2.27.3" /* Typing stubs for requests. */

  ].concat(options.devDeps ?? []),
  pip: false,
  pytest: false,
  mergify: false,
  poetry: true /* Use poetry as package manager, environment, and package builder. */,
  sample: false,
  stale: false,
  githubOptions: {
    pullRequestLint: false,
  },
  setuptools: false,
  venv: false,
});

customPythonProject.synth();
