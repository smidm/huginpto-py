import huginpto

def test_parse():
    pto = huginpto.HuginPto('test/kamera1-8.pto')
    assert len(pto.parsed['i']) == 8
    assert pto.parsed['i'][0]['n'].strip('"') == 'kamera1.png'
    
def test_get_correspondences():    
    import matplotlib.pylab as plt
    import numpy as np
    pto = huginpto.HuginPto('test/kamera1-8.pto')
    img = plt.imread('test/kamera2.png')
    plt.imshow(img)
    print pto.get_available_correspondence_pairs()
    c0, c1 = pto.get_correspondences(0, 1)
    c0 = np.array(c0)
    c1 = np.array(c1)
    plt.plot(c1[:, 0], c1[:, 1], '+')
    plt.show()
