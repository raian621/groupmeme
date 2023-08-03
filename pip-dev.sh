#!/usr/bin/bash

# -----------------------------------------------------------------------------
# pip-dev.sh
# -----------------------------------------------------------------------------
# Utility functions for seperating pip packages used in production and packages
# only used in development (such as test runners, coverage tools, linters, etc.)
#
# Preface:
#   pip doesn't have a "--save-dev" feature like npm, but you CAN have multiple
#   package requirement files wotj pip. If we maintain seperate files for 
#   production dependencies and extra development dependencies, we can pretty 
#   much get the same end result of using dev dependencies in npm.
#
# Usage:
#   source pip-env.sh
# -----------------------------------------------------------------------------


# Installs one or more production pip packages and saves the package names into
# 'requirements.txt'
#
# Usage:
#   pip-install <package-name(s)>
function pip-install {
  if [ $# -eq 0 ]; then
    echo 'Usage: pip-install <package-name(s)>'
    return
  elif [ $# -gt 1 ]; then
    for package in $@; do
      pip-install $package
    done
    return
  fi
  pip install $1 && pip freeze | grep $1 >> requirements.txt
}

# Installs one or more extra pip packages used in development and saves those
# package names into 'dev-requirements.txt'.
#
# Usage:
#   pip-install-dev <package-name(s)>
function pip-install-dev {
  if [ $# -eq 0 ]; then
    echo 'Usage: pip-install-dev <package-name(s)>'
    return
  elif [ $# -gt 1 ]; then
    for package in $@; do
      pip-install-dev $package
    done
    return
  fi
  pip install $1 && pip freeze | grep $1 >> requirements.dev.txt
}