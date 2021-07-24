from euros import it

echantillon=[
  ('0','zero euro'),
  (0.10,'dieci centesimi'),
  ('1','uno euro'),
  ('1000','mille euro'),
  (1e6,"un milione di euro"),
  ('1,000','mille euro'),
  (u'1\xa0000','mille euro'),
  ('200','duecento euro'),
  ('80','ottenta euro'),
  ('81,23','ottentuno euro e ventitré centesimi'),
  (1001e3,'un milione e mille euro'),
  (2228,'duemiladuecentoventotto euro'),
  (1e9,"un miliardo di euro"),
  (1000200,'un milione e duecento euro')
   ]

def test_it_conv():
  for t in echantillon:
    assert it.conv(t[0]) == t[1]
