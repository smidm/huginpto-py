Hugin .pto File Parser
======================

Useful for image correspondences definition.

Example usage:

```python
>>> import huginpto
>>> pto = huginpto.HuginPto('test/kamera1-8.pto')
>>> pto.parsed.keys()
['c', 'i', 'k', 'm', 'o', 'p', 'v']

>>> pto.parsed['c'][0]
{'N': '1',
'X': '565',
'Y': '749',
'n': '0',
't': '0',
'x': '1034',
'y': '619'}

>>> pto.parsed['i'][0]
{'E': ['ev0', 'r1', 'b1'],
'Ra': '0',
'Rb': '0',
'Rc': '0',
'Rd': '0',
'Re': '0',
'TrX': '0',
'TrY': '0',
'TrZ': '0',
'V': ['a1', 'b0', 'c0', 'd0', 'x0', 'y0', 'm5'],
'a': '0',
'b': '0',
'c': '0',
'd': '0',
'e': '0',
'f': '0',
'g': '0',
'h': '1024',
'j': '0',
'n': '"kamera1.png"',
'p': '0',
'r': '0',
't': '0',
'v': '50',
'w': '1280',
'y': '0'}

>>> import matplotlib.pylab as plt
>>> img = plt.imread('test/kamera2.png')
>>> plt.imshow(img)
>>> pto.get_available_correspondence_pairs()
[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4], [1, 5], [4, 6], [4, 5], [4, 7]]

>>> c0, c1 = pto.get_correspondences(0, 1)
>>> c0 = np.array(c0)
>>> c1 = np.array(c1)
>>> plt.plot(c1[:, 0], c1[:, 1], '+')
>>> plt.show()
```

![displayed correspondences](huginpto_correspondences.png)