# Publishing the Package to [PYPI](https://pypi.org/)

1. update the version in [setup.py](../setup.py)
2. run setup with `python setup.py sdist bdist_wheel`
3. publish to `testpypi`
4. publish to `pypi`

## Command Line Summary

```shell
python setup.py sdist bdist_wheel
```

```shell
twine upload -r testpypi dist/* -u $username -p $password
```

```shell
twine upload -r pypi dist/* -u $username -p $password
```
