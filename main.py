from src.data.db_connection import load_db_table
from config.config import get_project_root

PROJECT_ROOT = get_project_root()
df = load_db_table(config_db='database.ini', query='SELECT * FROM customer_contracts')
print(df)