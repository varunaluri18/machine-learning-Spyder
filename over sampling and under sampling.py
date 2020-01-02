# Over Sampling
from imblearn.over_sampling import RandomOverSampler
os = RandomOverSampler(ratio=1)
X1,Y1 = os.fit_sample(X,Y)


# Over Sampling
from imblearn.combine import SMOTETomek
smk= SMOTETomek(random_state=42)
X1,Y1 = smk.fit_sample(X,y)


# Under Sampling
from imblearn.under_sampling import NearMiss
us = NearMiss(random_state=42)
X1,Y1 = us.fit_sample(X,Y)
