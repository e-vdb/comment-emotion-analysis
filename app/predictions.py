import pickle

def load_pickle(filename):
  """Load  from disk."""
  return pickle.load(open(filename, 'rb'))
