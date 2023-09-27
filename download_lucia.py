from lsfb_dataset import Downloader

downloader = Downloader(
    dataset="isol",
    destination="/gpfs/projects/acad/lsfb/datasets/lsfb_v2_isol/isol",
    include_videos=True,
    include_raw_poses=True,
    include_cleaned_poses=True,
    skip_existing_files=False,
)

downloader.download()


downloader = Downloader(
    dataset="cont",
    destination="/gpfs/projects/acad/lsfb/datasets/lsfb_v2/cont",
    include_videos=True,
    include_raw_poses=True,
    include_cleaned_poses=True,
    skip_existing_files=False,
)
