#!/bin/bash

number1=$1
number2=$2
number3=$3

if [[ $number1 -gt $number2 ]] && [[ $number1 -gt $number3 ]]; then
    echo "$number1" "is greater than $number2 and $number3"
elif [[ $number2 -gt $number1 ]] && [[ $number2 -gt $number3 ]]; then
    echo "$number2" "is greater than $number1 and $number3"
else
    echo "$number3" "is greater than $number1 and $number2"
fi