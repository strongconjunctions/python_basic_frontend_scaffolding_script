"""Docstr."""

import subprocess


subprocess.call('mkdir app src js css sass build _modules _partials \
                _mixins', shell=True)
subprocess.call('touch index.html script.js index.sass _main.sass \
                _base.sass _mixins.sass', shell=True)
subprocess.call('touch .gitignore && touch README.md && echo \
### This is a Python scaffolding project. This setup is a basic \
setup for a front-end project involving JavaScript and SASS. Also \
threw in webpack just for kicks. > README.md && \
echo node_modules > .gitignore', shell=True)
subprocess.call('cp -R ./js/ ./build/ && mv ./css/ ./build/ && mv \
                ./js/ ./src/ && mv ./sass/ ./src/ && mv ./_modules/ \
                ./src/sass/ && mv ./_partials/ ./src/sass/ && mv \
                ./_mixins/ ./src/sass/ && mv index.html ./build/ && \
                mv index.sass ./src/sass/ && mv script.js ./src/js/ \
                && mv _main.sass ./src/sass/_modules/ && mv _base.sass \
                ./src/sass/_partials/ && mv _mixins.sass \
                ./src/sass/_mixins && mv ./build/ ./app/ && mv ./src/ \
                ./app/ && mv README.md ./app/ && mv .gitignore ./app/',
                shell=True)
subprocess.call('npm init -y && npm i -S webpack && mv package.json \
                ./app/ && mv ./node_modules/ ./app/', shell=True)
