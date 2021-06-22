# euros
[![](https://img.shields.io/badge/pypi-v1.0-blue)](https://pypi.org/project/euros/)

Converts any amount of euros from numbers into letters, using Python.

**Languages available :**
- french (fr)
- italian (it)
- english UK (en)

**Installation :**
```python
pip install euros
```

**Examples:**

```python
>>> from euros import fr,it,en

>>> fr.conv(120.99)
"cent vint euros et quatre-vingt-dix-neuf centimes"

>>> it.conv(23.81)
"ventitré euro e ottantuno centesimi"

>>> en.conv(1215.55)
"one thousand, two hundred and fifteen euros and fifty-five cents"
```
