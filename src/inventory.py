def summarize_inventory(items):
item_count = len(items)
total_units = sum(item["units"] for item in items)
low_stock_count = sum(1 for item in items if item["units"] < 10)
good_stock_count = item_count - low_stock_count
average_units = total_units / item_count

return {
    "item_count": item_count,
    "total_units": total_units,
    "low_stock_count": low_stock_count,
    "good_stock_count": good_stock_count,
    "average_units": average_units,
}
