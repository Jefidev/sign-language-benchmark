import math
import click
from experiments.prediction import poseVIT_prediction
import wandb

config_defaults = {
    "n_labels": 250,
    "seq_size": 32,
    "n_epochs": 10,
    "data_augmentation": False,
    "gradient_clip": False,
    "batch_size": 128,
    "embedding_size": 64,
    "dataset": "/home/jeromefink/Documents/unamur/signLanguage/Data/lsfb_v2/isol",
    "dry_run": True,
}


def train():
    wandb.init(config=config_defaults)
    poseVIT_prediction()


@click.command()
@click.option("-l", "--lables", default=250, help="Number of labels to predict")
@click.option(
    "-e",
    -"--experiment",
    default=" test ViT prediction",
    help="Name of the Experiment to run",
)
@click.option(
    "-d",
    "--dataset",
    default="/home/jeromefink/Documents/unamur/signLanguage/Data/lsfb_v2/isol",
    help="Path to the LSFB dataset",
)
@click.option("--dry-run", is_flag=True)
def run_experiment(labels, dataset, experiment, dry_run):
    """Run Sign Language Prediction Experiment"""

    # Sweep configuration
    sweep_config = {
        "method": "grid",
        "metric": {"name": "valid balanced accuracy", "goal": "maximize"},
        "parameters": {
            "seq_size": {"values": [32, 64, 128, 256]},
            "n_epochs": {"values": [10, 100, 1000]},
            "data_augmentation": {"values": [True, False]},
            "gradient_clip": {"values": [True, False]},
            "batch_size": {"values": [32, 64, 128, 256, 512]},
            "embedding_size": {"values": [32, 64, 128, 256]},
        },
    }

    config_defaults["n_labels"] = labels
    config_defaults["dataset"] = dataset
    config_defaults["dry_run"] = dry_run

    sweep_id = wandb.sweep(sweep_config, project=experiment)

    # run sweep
    wandb.agent(sweep_id, function=train)


if __name__ == "__main__":
    run_experiment()