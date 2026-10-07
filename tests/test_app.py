from app import get_inventory
from app import get_health_status


def test_health_status_is_healthy():
    status = get_health_status()

    assert status == {"status": "healthy"}


def test_inventory_has_items():
    inventory = get_inventory()

    assert len(inventory) > 0


def test_inventory_items_have_required_fields():
    item = get_inventory()[0]

    assert "id" in item
    assert "name" in item
    assert "quantity" in item


def test_inventory_quantity_is_a_number():
    item = get_inventory()[0]

    assert isinstance(item["quantity"], int)
