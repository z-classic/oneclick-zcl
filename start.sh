#!/bin/bash

# TODO Start from a config file

# Running optiminer-equihash-2.1.2: https://github.com/Optiminer/OptiminerEquihash
./optiminer-equihash -s $POOL -u $USER -p $PASSWORD --watchdog-timeout 30 -a equihash200_9 --watchdog-cmd "./watchdog-cmd.sh" $ADDITIONAL $@
