#!/bin/bash

mapfile -t mylist < ttbar.dat

echo ${mylist[1]}
