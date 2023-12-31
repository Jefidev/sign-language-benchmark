import math
import click
from experiments.prediction.vit_experiment import start_run
import wandb

config_defaults = {
    "n_labels": 250,
    "seq_size": 32,
    "n_epochs": 300,
    "data_augmentation": False,
    "gradient_clip": False,
    "batch_size": 128,
    "embedding_size": 64,
    "dataset": "/home/jeromefink/Documents/unamur/signLanguage/Data/lsfb_v2/isol",
    "dry_run": True,
}


def train():
    wandb.init(config=config_defaults)
    start_run()


@click.command()
@click.option("-l", "--labels", default=250, help="Number of labels to predict")
@click.option(
    "-e",
    "--experiment",
    default="test-run",
    help="Name of the Experiment to run",
)
@click.option(
    "-d",
    "--dataset",
    default="/home/jeromefink/Documents/unamur/signLanguage/Data/lsfb_v2/isol",
    help="Path to the LSFB dataset",
)
@click.option("--dry-run", is_flag=True)
def run_experiment(labels, experiment, dataset, dry_run):
    """Run Sign Language Prediction Experiment"""

    # Sweep configuration
    sweep_config = {
        "method": "bayes",
        "metric": {"name": "valid balanced accuracy", "goal": "maximize"},
        "parameters": {
            "seq_size": {"values": [16, 32, 64]},
            "data_augmentation": {"values": [True, False]},
            "gradient_clip": {"values": [True, False]},
            "batch_size": {"values": [128, 256, 512]},
            "embedding_size": {"values": [32, 64, 128, 256]},
        },
    }

    config_defaults["n_labels"] = labels
    config_defaults["dataset"] = dataset
    config_defaults["dry_run"] = dry_run

    sweep_id = wandb.sweep(sweep_config, project=experiment)

    # run sweep
    wandb.agent(sweep_id, function=train, count=20)


if __name__ == "__main__":
    run_experiment()
