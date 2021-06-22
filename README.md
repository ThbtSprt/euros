# euros
[![](https://img.shields.io/badge/pypi-v0.0.5-blue)](https://pypi.org/project/euros/)

Converts any amount of euros from numbers into letters, using Python.

**Languages available :**
- french (fr)
- italian (it)

**Installation :**
```python
pip install euros
```

**Examples:**

```python
>>> from euros import fr,it

>>> fr.conv(10)
"dix euros"

>>> fr.conv(120.99)
"cent vint euros et quatre-vingt-dix-neuf centimes"

>>> fr.conv(1000000.01)
"un million d'euros et un centime"

>>> it.conv(23.81)
"ventitré euro e ottantuno centesimi"
```
