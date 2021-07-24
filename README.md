# euros
[![](https://img.shields.io/badge/pypi-v1.1-blue)](https://pypi.org/project/euros/)

Converts any amount of euros from numbers into letters, using Python.

**Languages available :**
- [x] french (fr)
- [x] italian (it)
- [x] english UK (en)

**Installation :**
```python
pip install euros
```

**Examples:**

```python
>>> from euros import fr,it,en

>>> fr.conv(120.99)
"cent vingt euros et quatre-vingt-dix-neuf centimes"

>>> it.conv(23.81)
"ventitré euro e ottantuno centesimi"

>>> en.conv(1215.55)
"one thousand, two hundred and fifteen euros and fifty-five cents"
```
