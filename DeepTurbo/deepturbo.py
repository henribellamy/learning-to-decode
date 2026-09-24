import numpy as np


def P (s, k1 = 8, k2 = 223):
    premiers = [0, 31, 37, 43, 47, 53, 59, 61, 67]
    m = (s-1)%2
    i = np.floor ((s-1)/(2*k2))
    j = np.floor ((s-1)/2) - i*k2
    t = (19*i +1) % (k1/2)
    q = t%8 +1
    c = (premiers[int (q)]*j + 21*m)%k2
    pi = 2*(t+c*(k1/2) + 1) -m
    return int (pi)

perm     = np.array([P(s) - 1 for s in range(1, 1785)])
perm_inv = np.argsort(perm)


def interleaver_batch(x):        # (B, 1784)
    return x[:, perm]

def deinterleaver_batch(x):      # (B, 1784)
    return x[:, perm_inv]

def extrait_batch(v):            # v : (B, 1784, 3)
    c0  = v[:, :, 0]             # (B, 1784)
    c1  = v[:, :, 1]
    c2  = v[:, :, 2]
    c0i = interleaver_batch(c0)  # (B, 1784)

    e1 = np.stack([c0,  c1], axis=-1)   # (B, 1784, 2)
    e2 = np.stack([c0i, c2], axis=-1)   # (B, 1784, 2)
    return e1, e2


def decode(v, ni, network, Lc):
    # v : (B, 1784, 3)
    B = v.shape[0]

    e1, e2 = extrait_batch(v)           # (B, 1784, 2)

    Lpriori = np.zeros((B, 1784))

    for k in range(ni):
        # --- décodeur 1 ---
        enter      = np.concatenate([e1, Lpriori[:, :, None]], axis=-1)  # (B, 1784, 3)
        Lsachant = network.predict(enter, verbose=0).squeeze(-1)  # (B, 1784)         
        Lextrin    = Lsachant - Lpriori - Lc * e1[:, :, 0]
        Lpriori    = interleaver_batch(Lextrin)

        # --- décodeur 2 ---
        enter      = np.concatenate([e2, Lpriori[:, :, None]], axis=-1)
        Lsachant = network.predict(enter, verbose=0).squeeze(-1)  # (B, 1784)
        Lextrin    = Lsachant - Lpriori - Lc * e2[:, :, 0]
        Lpriori    = deinterleaver_batch(Lextrin)

    return deinterleaver_batch(Lsachant)  # (B, 1784)