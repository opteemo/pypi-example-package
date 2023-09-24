# Example package

Simple package to test publishing on PyPI.

## Poetry configuration

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi <token>
poetry publish --build -r testpypi 
```

## References

- [Stackoverflow - How to package a Python wheel to be executable as cli using poetry?](https://stackoverflow.com/questions/70398864/how-to-package-a-python-wheel-to-be-executable-as-cli-using-poetry)