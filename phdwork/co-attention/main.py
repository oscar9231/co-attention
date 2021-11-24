import h5py
f = h5py.File('/Users/liyuanchao/Documents/Corpus/CMU-MOSEI/audio/audio_test.h5', 'r')
i = 0
for key in f.keys():
    print(f[key][0])
    # print(f[key])