from efficient_evolution.amis import reconstruct_multi_models


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Recommend substitutions to a wildtype sequence")
    parser.add_argument("sequence", type=str, help="Wildtype sequence")
    parser.add_argument(
        "--model-names",
        type=str,
        default=[
            "esm1b",
            "esm1v1",
            "esm1v2",
            "esm1v3",
            "esm1v4",
            "esm1v5",
        ],
        nargs="+",
        help="Type of language model (e.g., esm1b, esm1v1)",
    )
    parser.add_argument("--alpha", type=float, default=None, help="alpha stringency parameter")
    args = parser.parse_args()
    return args


def recommend(sequence, model_names, alpha=None):
    mutations_models = reconstruct_multi_models(
        sequence,
        model_names,
        alpha=alpha,
    )
    for k, v in sorted(mutations_models.items(), key=lambda item: -item[1]):
        mut_str = f"{k[1]}{k[0] + 1}{k[2]}"
        print(f"{mut_str}\t{v}")

    return mutations_models


if __name__ == "__main__":
    args = parse_args()

    mutations_models = reconstruct_multi_models(
        args.sequence,
        args.model_names,
        alpha=args.alpha,
    )
    for k, v in sorted(mutations_models.items(), key=lambda item: -item[1]):
        mut_str = f"{k[1]}{k[0] + 1}{k[2]}"
        print(f"{mut_str}\t{v}")
