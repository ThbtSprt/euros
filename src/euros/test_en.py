from euros import en

echantillon=[
  ('0','zero euro'),
  (0.10,'ten cents'),
  ('1','one euro'),
  ('1000','a thousand euros'),
  (1e6,"one million euros"),
  ('1,000','a thousand euros'),
  (u'1\xa0000','a thousand euros'),
  ('200','two hundred euros'),
  ('80','eighty euros'),
  ('84,99','eighty-four euros and ninety-nine cents'),
  (1001e3,'one million thousand euros'),
  (1e9,"one billion euros"),
  (2200,'two thousand two hundred euros')
   ]

def test_fr_conv():
  for t in echantillon:
    assert en.conv(t[0]) == t[1]
