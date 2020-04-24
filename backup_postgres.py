import subprocess
import datetime
from test_pitr.base import internal_connection_string

subprocess.call(["docker-compose", "exec", "postgres", "bash", "-c",
                 f"pg_basebackup --dbname={internal_connection_string} -Ft -X none -D - | gzip > /opt/pgbackup/backup{datetime.datetime.utcnow().timestamp()}.tar.gz"])
