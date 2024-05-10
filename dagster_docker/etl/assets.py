from dagster import asset


@asset
def my_first_asset():
    return [1, 2, 3]