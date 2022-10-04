#!/bin/bash

rm test.py
cd core
mv settings.py basesettings.py
mv cloudsettings.py settings.py
cd ../../
git add .
git commit -m "Done for the first version of the application"
git push --set-upstream origin version_1.1

cd src/core/
mv settings.py cloudsettings.py
mv basesettings.py settings.py
cd ..
clear