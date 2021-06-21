# euros
[![](https://img.shields.io/badge/pypi-v0.0.5-blue)](https://pypi.org/project/euros/)

Simple script python destiné à convertir des chiffres en lettres, pour désigner un montant en euros en français littéral respectant les règles orthographiques.

Installation :
```python
pip install euros
```

Exemples d'utilisation :

```python
>>> from euros.fr import conv

>>> conv(10) 
"dix euros"

>>> conv(120.99) 
"cent vint euros et quatre-vingt-dix-neuf centimes"

>>> conv(1000000.01) 
"un million d'euros et un centime"
```
