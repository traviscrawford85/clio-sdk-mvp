import pytest
from pydantic import ValidationError

from clio_sdk.adapters.adapter_activity import (
    ClioActivity,  # Import ClioActivity if it exists in adapter_activity
)
from clio_sdk.adapters.adapter_activity import (
    clio_to_internal_from_activity,
    internal_to_clio_to_activity,
)
from clio_sdk.generated_models.activity import Activity


@pytest.mark.parametrize("note, price", [
    ("test note", 100.0),
    ("", 0.0),
    (None, 55.5)
])
def test_roundtrip_activity_variants(note, price):
    clio = ClioActivity(id=12356956, note=note, billed=True, price=price)
    internal = clio_to_internal_from_activity(clio)
    assert isinstance(internal, Activity)
    clio_again = internal_to_clio_to_activity(internal)
    assert clio_again.model_dump() == clio.model_dump()

def test_invalid_activity_input():
    with pytest.raises(ValidationError):
        ClioActivity(id=123, billed=None)  # invalid: billed must be bool, using None to trigger validation
