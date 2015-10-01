#!/bin/bash
until /home/pi/git/rfid/pyrfid_demo.py; do
    echo "'pyrfid_demo.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
