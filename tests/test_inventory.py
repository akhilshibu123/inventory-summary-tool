from src.inventory import summarize_inventory

def test_normal_inventory():
items = [
{"name": "Pens", "units": 5},
{"name": "Books", "units": 20},
{"name": "Bags", "units": 15},
]

result = summarize_inventory(items)

assert result["item_count"] == 3
assert result["total_units"] == 40
assert result["low_stock_count"] == 1
assert result["good_stock_count"] == 2
assert result["average_units"] == 40 / 3
