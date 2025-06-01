# clio_sdk/queries_db/batch.py
from .matters import get_matter_by_id_db


def batch_get_matters_db(ids: list[int]):
    return [get_matter_by_id_db(id) for id in ids]