from sqlalchemy import create_engine, inspect
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os

# --- CONFIG ---
DB_URL = 'sqlite:///./app.db'
TEMPLATE_PATH = 'scripts/db_scripts/sqlalchemy_model.py.jinja'
OUTPUT_DIR = 'database/generated_models'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- JINJA ENV ---
env = Environment(loader=FileSystemLoader(Path(TEMPLATE_PATH).parent))
template = env.get_template(Path(TEMPLATE_PATH).name)

# --- SQLALCHEMY INSPECTION ---
engine = create_engine(DB_URL)
inspector = inspect(engine)

def snake_to_camel(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def get_column_type(col):
    t = str(col['type'])
    if 'INTEGER' in t:
        return 'Integer'
    if 'TEXT' in t:
        return 'Text'
    if 'REAL' in t or 'FLOAT' in t:
        return 'Float'
    if 'DATETIME' in t:
        return 'DateTime'
    return 'String'

for table_name in inspector.get_table_names():
    columns = inspector.get_columns(table_name)
    class_name = snake_to_camel(table_name)
    rendered = template.render(
        class_name=class_name,
        table_name=table_name,
        columns=[{
            'name': col['name'],
            'type': get_column_type(col),
            'primary_key': col.get('primary_key', False),
            'nullable': col.get('nullable', True)
        } for col in columns],
        columns_imports=['Integer', 'Text', 'Float', 'DateTime', 'String']
    )
    out_path = Path(OUTPUT_DIR) / f"{table_name}.py"
    out_path.write_text(rendered.strip() + '\n')
    print(f"✅ Generated model for table: {table_name}")
