import os

models_dir = 'clio_sdk/models'
init_file = os.path.join(models_dir, '__init__.py')

with open(init_file, 'w') as f:
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            f.write(f'from .{module_name} import *\n')
