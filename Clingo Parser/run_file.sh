#!/bin/sh

#clingo_input_fname = $1
#project_name = $2

cp $1 Mini\ Workflow/clingo_input/$2.lp4

echo "Copying Done"

clingo -n ${3:-0} -W none Mini\ Workflow/clingo_input/$2.lp4 > Mini\ Workflow/clingo_output/$2.txt

echo "Clingo Ouput Done"

python Preprocessing.py Mini\ Workflow/clingo_output/$2.txt

echo "Preprocessing Done"

echo "Enter a comma-separated list of formats you want to export in. Options: sql, csv, h5, msg, pkl"

python AntlrClingo.py Mini\ Workflow/clingo_output/$2.txt $2 > Mini\ Workflow/parser_output/$2.txt

