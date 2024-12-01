import os
import uuid
from pathlib import Path

import boto3
from tqdm import tqdm

from c214_lab_project.domain.repositories.r2_repository import R2Repository


class CloudflareR2Repository(R2Repository):
    def __init__(self) -> None:
        super(CloudflareR2Repository, self).__init__()

        self._connection = boto3.client(
            "s3",
            endpoint_url="https://79cce192eef74350c0ad124200ccebb7.r2.cloudflarestorage.com",
            aws_access_key_id="0d6a57b3b38dd24b43a6e064b467c106",
            aws_secret_access_key="1d1ad1716c0d672ac2d56fe5c04af1b0c3adb935df5b21318be4ef9f9ac213de",
            region_name="auto",
        )

    def upload(self, filepath: Path, file_id: str) -> None:
        file_size = os.path.getsize(filepath)
        progress_bar = tqdm(
            total=file_size, unit="B", unit_scale=True, desc="Uploading"
        )

        def callback(bytes_transferred):
            progress_bar.update(bytes_transferred)

        file_object_id = file_id
        self._connection.upload_file(
            Filename=str(filepath.absolute()),
            Bucket="black-hole",
            Key=file_object_id,
            Callback=callback,
        )
        progress_bar.close()
        return file_object_id

    def download(self, file_object_id: str) -> bool:
        download_folder = (
            Path(os.path.expanduser("~/Downloads")) / file_object_id
        )

        with open(download_folder, "wb") as f:
            response = self._connection.get_object(
                Bucket="black-hole", Key=file_object_id
            )
            file_size = response["ContentLength"]
            progress_bar = tqdm(
                total=file_size, unit="B", unit_scale=True, desc="Downloading"
            )

            for chunk in response["Body"].iter_chunks(chunk_size=8192):
                f.write(chunk)
                progress_bar.update(len(chunk))

            progress_bar.close()
