#!/bin/bash
SCRIPT_PATH=$(readlink -fn $0)
SCRIPT_HOME=$(dirname $SCRIPT_PATH)
#echo "SCRIPT_HOME = $SCRIPT_HOME"
cd $SCRIPT_HOME

find . -name '*.py' -print0 | xargs -0 black
