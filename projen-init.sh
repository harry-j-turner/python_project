#!/bin/sh
if [[ ${PWD##*/} = projen-python-submodule ]]; then
  cd ..
fi
ln -s ./projen-python-submodule/.projenrc.js .projenrc.js
pwd
cat <<EOF >.projenrc.projdata
{
  "name": "$(echo ${PWD##*/})",
  "version": "1.0.0",
  "deps": [],
  "defaultDockerPort": 8000
}
EOF

projen
