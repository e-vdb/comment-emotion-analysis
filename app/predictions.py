import pickle


def load_pickle(filename: str):
  """
  Load a file  from disk.

  Parameters
  ----------
  filename: str
    Name of the file that is loaded.
  Returns
  -------

  """
  return pickle.load(open(filename, 'rb'))


def make_prediction(model, encoder, entry):
  y_pred = model.predict([entry])
  output = encoder.inverse_transform(y_pred.reshape(-1, 1))[0][0]
  return output
