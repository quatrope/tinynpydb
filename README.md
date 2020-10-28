# The `tinynpydb` project
`tinynpydb` _(tiny-en-py-db)_ is a tiny picke-based numpy array database

## Installing

Simply clone and from within the repo
```
pip install -e .
```

## Quickstart

Starting a DB is easy:

```python
# import and create example
import tinynpydb as tnpdb

array = [1, 2, 3]

# start DB and dump array!
npdb = tnpdb.NumPyDB('testnpdb', mode="store")
npdb.dump(array, 0)

# retrieve array!
loaded_array = npdb.load(0)
print(loaded_array)
```

Re-using a DB is easy too:

```python
# import and create example
import tinynpydb as tnpdb

# start DB in loading mode
npdb = tnpdb.NumPyDB('testnpdb', mode="load")

# retrieve array!
loaded_array = npdb.load(0)
print(loaded_array)
```