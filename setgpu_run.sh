#!/bin/sh

export CUDA_VISIBLE_DEVICES=$1
export RUN_PROGRAM
${PYTHON:=python} $RUN_PROGRAM

