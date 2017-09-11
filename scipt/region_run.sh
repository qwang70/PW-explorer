#!/bin/bash
DLVPARSER="../Dlv Parser"
DLV="$DLVPARSER/dlv_bin/dlv.i386-apple-darwin.bin"
PWE="$DLVPARSER/dlv_parser/pwe"
MINIWORKFLOW="$DLVPARSER/Mini Workflow"
function getBaseName() 
{
    local fulfile=`ls $1/0-Input/*.txt`
    local filename=$(basename "$fulfile")
    local filename="${filename%.*}"
    echo "$filename"
}

# list of project names of CEN-NDC-regions with exactly one restriction being removed
FOLDER_LOCS=("../iConference" "../CEN-TZ_Regions_Example_DLV" "../Nico_Examples_DLV/MinArt0" "../Nico_Examples_DLV/Original")
QUERY_FOLDER="sqlQuery"
for FOLDER_LOC in "${FOLDER_LOCS[@]}"
do
    for PROJECT_PATH in $FOLDER_LOC/20*
    do
        PROJECT_NAME=${PROJECT_PATH##*/}
        echo $PROJECT_NAME
        mkdir -p $PROJECT_PATH/query_output
        OUTPUT_FOLDER=$PROJECT_PATH/query_output
        PROJECT_INPUT="$PROJECT_PATH/1-ASP-input-code"
        #MIR_FILE="$PROJECT_PATH/3-MIR/CEN-NDC-regions_mir.csv"
        PW_OUTPUT="$PROJECT_PATH/4-PWs"
        # Find project file name without extension
        # The name is reused when outputing pw worlds
        BASENAME=$(getBaseName $PROJECT_PATH) 
        # output ASP file
        "$DLV" -silent $PROJECT_INPUT/${BASENAME}_pw.dlv $PROJECT_INPUT/${BASENAME}_ixswitch.dlv $PROJECT_INPUT/${BASENAME}_pwswitch.dlv -filter=rel > "$MINIWORKFLOW"/dlv_output/$PROJECT_NAME.asp
        # parse the ASP file and output files in other common format
        "$PWE" export "$MINIWORKFLOW"/dlv_output/$PROJECT_NAME.asp -sql -csv

        # output region type and numbers from sqlite
#        echo "#possible world, #congruent regions"
        "$PWE" sqlQuery "$MINIWORKFLOW"/parser_output/sql_exports/$PROJECT_NAME/$PROJECT_NAME.db -f $QUERY_FOLDER/congruent.sql > $OUTPUT_FOLDER/congruent_sql.csv
#        echo "#possible world, #overlapped regions"
        "$PWE" sqlQuery "$MINIWORKFLOW"/parser_output/sql_exports/$PROJECT_NAME/$PROJECT_NAME.db -f $QUERY_FOLDER/overlap.sql > $OUTPUT_FOLDER/overlap_sql.csv
#        echo "#possible world, #subset regions"
        "$PWE" sqlQuery "$MINIWORKFLOW"/parser_output/sql_exports/$PROJECT_NAME/$PROJECT_NAME.db -f $QUERY_FOLDER/subset.sql > $OUTPUT_FOLDER/subset_sql.csv
#        echo "#possible world, #all not equal relations"
        "$PWE" sqlQuery "$MINIWORKFLOW"/parser_output/sql_exports/$PROJECT_NAME/$PROJECT_NAME.db -f $QUERY_FOLDER/allNotEqualRelationCount.sql > $OUTPUT_FOLDER/notEqual_sql.csv
        #echo "Unambiguous relations from csv file"
        #python csvQuery.py $MIR_FILE
        
        # output region type and numbers from gv
        N_PW=`ls $PW_OUTPUT/*.gv | wc -l`
        python3 ../extract_from_gv2.py $PROJECT_PATH $BASENAME $N_PW  > $OUTPUT_FOLDER/relation_gv.txt
        # output region type and numbers from yaml
        N_PW=`ls $PW_OUTPUT/*.yaml | wc -l`
        python3 ../extract_stats_from_yaml2.py $PROJECT_PATH $BASENAME $N_PW
    done
done
