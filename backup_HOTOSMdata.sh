#/bin/sh

mount -v /dev/sdb1 /home/backup_drive

BACKUP_TIME=$(date +%y-%m-%d)

DESTINATION=/home/backup_drive/HOTOSMdata_$BACKUP_TIME.tar.gz

SOURCEFOLDER=/home/mnt/HOTOSM_data

echo "Backing up $SOURCEFOLDER to $DESTINATION"
date
echo

tar -cvpzf $DESTINATION $SOURCEFOLDER

echo "Backup finished."
 ls -lh $DESTINATION
