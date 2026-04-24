#!/bin/bash

# Variables
BUCKET_NAME="dr-backup-bucket"
BACKUP_FILE="backup_$(date +%F_%T).tar.gz"
SOURCE_DIR="/var/www/html"

echo "Starting backup process..."

# Create backup
tar -czvf $BACKUP_FILE $SOURCE_DIR

# Upload to S3
aws s3 cp $BACKUP_FILE s3://$BUCKET_NAME/

echo "Backup uploaded to S3 successfully!"

# Cleanup local backup
rm $BACKUP_FILE

echo "Backup process completed!"
