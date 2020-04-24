import subprocess

subprocess.call(["docker-compose", "exec", "postgres", "bash", "-c", "systemctl stop postgresql@11-main"])
subprocess.call(["docker-compose", "exec", "postgres", "bash", "-c", "rm -rf /opt/pgdata"])
