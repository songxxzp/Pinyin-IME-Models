from utils import get_prefix_model_value, load_probabilistic_model

def main():
    probabilistic_model = load_probabilistic_model("trigram_std/probabilistic_model.gz")
    prob = get_prefix_model_value(
        model=probabilistic_model,
        prefix="北京",
        token="是"
    )
    print("p({}|{}) = {}".format("是", "北京", str(prob)))

if __name__ == "__main__":
    main()
