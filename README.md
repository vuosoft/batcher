# Batcher utility

Batcher library takes in an array of records of variable size and splits the input to batches of records (array of arrays) suitably sized for delivery to a system which has following limits:

maximum size of output record is 1 MB, larger records should be discarded
maximum size of output batch is 5 MB
maximum number of records in an output batch is 500

Input for the library is: [<record1>, <record2>, <record3>, ... , <recordn>]

Output is: [<batch1>, <batch2>, ..., <batchn>] where each batch is an array of records just like in the input.

The records are assumed to be strings of variable length and they pass intact through the system and records stays in the order that they arrive.

## To install

```bash
pip3 install -i https://test.pypi.org/simple/ batcher==0.0.2
```

## To use

```python
from batcherlib import main
response = main.batcher(array)
```

## To build the library and push to test PyPI

```bash
cd  batcherpack
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```
