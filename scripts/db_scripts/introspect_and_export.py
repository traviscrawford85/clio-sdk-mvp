from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///./app.db')
inspector = inspect(engine)

for table_name in inspector.get_table_names():
    columns = inspector.get_columns(table_name)
    # Build a schema dict or render a Jinja template for each table