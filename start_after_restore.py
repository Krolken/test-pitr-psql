import subprocess
from test_pitr.base import internal_connection_string

subprocess.call(["docker-compose", "exec", "postgres", "bash", "-c", f"psql {internal_connection_string} -c 'select pg_wal_replay_resume();'"])
