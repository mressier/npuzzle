#!/bin/bash

typeset DIR="/Users/mressier/Documents/npuzzle/"
typeset NAME="npuzzle.py"
typeset FILE_OPTION="-f"

typeset NPUZZLE="${DIR}/${NAME}"
typeset TESTS_DIR="${DIR}/resources/"
typeset MAPS_SUCCESS_DIR="${TESTS_DIR}/maps/success/"
typeset MAPS_SUCCESS="${MAPS_SUCCESS_DIR}*"
typeset MAPS_FAILURE_DIR="${TESTS_DIR}/maps/failure/"
typeset MAPS_FAILURE="${MAPS_FAILURE_DIR}*"

## TOOLS
typeset RED_COLOR="\033[31m"
typeset GREEN_COLOR="\033[32m"
typeset CLEAR_COLOR="\033[0m"

typeset ERROR_FILE="/tmp/stderr"

function error
{
    echo -e "${RED_COLOR}FAIL:${CLEAR_COLOR}" $*
}

function success
{
    echo -e "${GREEN_COLOR}OK:${CLEAR_COLOR}" $*
}

function execute
{
    (( $# == 1 )) || { error "execute: bad number of arguments"; }

    typeset map=$1

    python ${NPUZZLE} ${FILE_OPTION} ${map} 2>${ERROR_FILE} 1>/dev/null
    typeset -i PYTHON_EXIT_STATUS=$?
    
    # test for python error
    grep -iq "Traceback" ${ERROR_FILE}
    typeset -i EXIT_STATUS=$?
    (( ${EXIT_STATUS} == 0 )) && return 255

    return ${PYTHON_EXIT_STATUS}
}

##
## MAIN
##

[[ -e ${DIR} ]] || { error "${DIR} doesn't exist"; exit 1; }

for map in ${MAPS_FAILURE}
do
    execute "${map}"
    typeset EXIT_STATUS=$?
    typeset MAP_NAME=${map##"${MAPS_FAILURE_DIR}"}

    if (( ${EXIT_STATUS} == 255 ))
    then
        error "map ${MAP_NAME}: python error"
    elif (( ${EXIT_STATUS} != 0 ))
    then
        success "map ${MAP_NAME} fail as expected"
    else
        error "map ${MAP_NAME} return ${EXIT_STATUS} - failure expected"
    fi
done

for map in ${MAPS_SUCCESS}
do
    execute "${map}"
    typeset EXIT_STATUS=$?
    typeset MAP_NAME=${map##"${MAPS_SUCCESS_DIR}"}

    if (( ${EXIT_STATUS} == 255 ))
    then
        error "map ${MAP_NAME}: python error"
    elif (( ${EXIT_STATUS} != 0 ))
    then
        error "map ${MAP_NAME} return ${EXIT_STATUS} - success expected"
    else
        success "map ${MAP_NAME} success"
    fi
done
