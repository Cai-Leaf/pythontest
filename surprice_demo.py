from surprise import SVD, KNNBasic, SVDpp, KNNBaseline
from surprise import Dataset
from surprise import evaluate, print_perf
import time


# Load the movielens-100k dataset (download it if needed),
# and split it into 3 folds for cross-validation.
data = Dataset.load_builtin('ml-1m')
print(len(data.raw_ratings))
 
data.split(n_folds=5)

# We'll use the famous SVD algorithm.
algo = SVDpp()

# bsl_options = {'method': 'als',
#                'n_epochs': 20,
#                }
# sim_options = {'name': 'pearson_baseline', 'user_based': False}
# algo = KNNBasic(sim_options=sim_options)

# Evaluate performances of our algorithm on the dataset.
start = time.time()
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

print_perf(perf)
print('time', (time.time()-start)/60)
# 15:58
