from euros import fr

echantillon=[
  ('0','zéro euro'),
  (0.10,'dix centimes'),
  ('1','un euro'),
  ('1000','mille euros'),
  (1e6,"un million d'euros"),
  ('1,000','mille euros'),
  (2000,'deux mille euros'),
  (u'1\xa0000','mille euros'),
  ('200','deux cents euros'),
  ('80','quatre-vingts euros'),
  ('84,99','quatre-vingt-quatre euros et quatre-vingt-dix-neuf centimes'),
  (1001e3,'un million mille euros'),
  (1e9,"un milliard d'euros"),
  (2200,'deux mille deux cents euros'),
  (1000200,'un million deux cents euros')
   ]

def test_fr_conv():
  for t in echantillon:
    assert fr.conv(t[0]) == t[1]
