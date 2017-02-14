#!/bin/bash

DATE=$(date '+%Y%m%d-%Hh%M')
TAR_NAME="world-${DATE}.tar.gz"
SCRIPT_DIR="/home/lacsap/mcscript/"
MC_DIR="/docker_data/minecraft/"

# Reading ftp credential file
source ~/.mcscript/ftp


echo "[$(date '+%Y%m%d-%Hh%M')] - Starting world backup"
${SCRIPT_DIR}/rconcmd.py "say [$(date '+%Y%m%d-%Hh%M')] - World backup in progress..."

echo "[$(date '+%Y%m%d-%Hh%M')] - Forcing world save"
${SCRIPT_DIR}/rconcmd.py save-all

echo "[$(date '+%Y%m%d-%Hh%M')] - Stopping automatic world saving"
${SCRIPT_DIR}/rconcmd.py save-off
sleep 5

echo "[$(date '+%Y%m%d-%Hh%M')] - Creating ${TAR_NAME} file"
cd ${MC_DIR}

tar -zcf ${TAR_NAME} world
if [ $? -ne 0 ]; then echo "Error zipping the world dir"; exit 1; fi

echo "[$(date '+%Y%m%d-%Hh%M')] - Starting automatic world saving"
${SCRIPT_DIR}/rconcmd.py save-on


echo "[$(date '+%Y%m%d-%Hh%M')] - Sending ${TAR_NAME} via FTP"
ftp -inv $HOST << EOF

user $USER $PASS

cd /typhoon/minecraftbk/
put ${TAR_NAME}
bye

EOF
if [ $? -ne 0 ]; then echo "Error during FTP"; exit 1; fi

echo "[$(date '+%Y%m%d-%Hh%M')] - Deleting local zip file"
cd ${MC_DIR}
rm ${TAR_NAME}

echo "[$(date '+%Y%m%d-%Hh%M')] - Backup done!"
${SCRIPT_DIR}/rconcmd.py "say [$(date '+%Y%m%d-%Hh%M')] - World backup Done !"

