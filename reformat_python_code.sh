#!/bin/bash
SCRIPT_PATH=$(readlink -fn $0)
SCRIPT_HOME=$(dirname $SCRIPT_PATH)
#echo "SCRIPT_HOME = $SCRIPT_HOME"
cd $SCRIPT_HOME

echo "Starting the process of reformatting the entire python codebase"

echo "Reformatting code in the directory ${SCRIPT_HOME}/Arrays"
find ./Arrays/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Backtracking"
find ./Backtracking/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Bit_Magic"
find ./Bit_Magic/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Divide_and_Conquer"
find ./Divide_and_Conquer/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Dynamic_Programming"
find ./Dynamic_Programming/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Graph"
find ./Graph/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Greedy"
find ./Greedy/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Hashing"
find ./Hashing/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Heap"
find ./Heap/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Linked_List"
find ./Linked_List/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Recursion"
find ./Recursion/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Stack_and_Queue"
find ./Stack_and_Queue/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/String"
find ./String/ -name '*.py' -print0 | xargs -0 black

echo "Reformatting code in the directory ${SCRIPT_HOME}/Tree_and_BST"
find ./Tree_and_BST/ -name '*.py' -print0 | xargs -0 black

echo "Finished the process of reformatting the entire python codebase"
