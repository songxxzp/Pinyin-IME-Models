import pickle
import gzip


def load_frequency_model(model_path):
    with gzip.open(model_path, "rb") as file:
        frequency_dict = pickle.load(file)
        conditional_frequency_dict = frequency_dict["conditional_frequency_dict"]
    return conditional_frequency_dict


def load_probabilistic_model(model_path):
    with gzip.open(model_path, "rb") as file:
        probabilistic_dict = pickle.load(file)
        conditional_probabilistic_model = probabilistic_dict["conditional_probabilistic_dict"]
    return conditional_probabilistic_model


def get_prefix_model_value(model, prefix, token):
    """
        return p(token|prefix)
    """
    if prefix not in model or token not in model[prefix]:
        return 0
    return model[prefix][token]
