import subprocess
from datetime import datetime

datetime_str = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

alembic_migration_commands = [
    f"alembic revision --autogenerate -m {datetime_str}",
    "alembic upgrade head",
]

print("RUNNING STARTUP")

for command in alembic_migration_commands:
    subprocess.run(command.split(" "))
