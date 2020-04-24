
with open('pgdata/recovery.conf', 'w+') as f:
    f.write("restore_command = 'cp /opt/waldir_archive/%f %p'\n")
    f.write("recovery_target_time = '2020-04-24 13:58:00 CEST'")


# tar xvfz pgbackup/backup1587729433.116587.tar.gz -C /pgdata/