import json
import os
from pathlib import Path

import rich
import typer

from c214_lab_project.application.database.repositories.cloudflare_r2_repository import (
    CloudflareR2Repository,
)
from c214_lab_project.application.database.repositories.peewee_file_repository import (
    PeeweeFileRepository,
)
from c214_lab_project.application.database.repositories.peewee_shared_link_repository import (
    PeeweeSharedLinkRepository,
)
from c214_lab_project.application.database.repositories.peewee_user_repository import (
    PeeweeUserRepository,
)
from c214_lab_project.domain.mappers.user_mapper import UserMapper
from c214_lab_project.domain.use_cases.file.download_file_use_case import (
    DownloadFileUseCase,
)
from c214_lab_project.domain.use_cases.file.upload_file_use_case import (
    UploadFileUseCase,
)
from c214_lab_project.domain.use_cases.user.login_user_use_case import (
    LoginUserUseCase,
)
from tests.factories.make_user import make_user

app = typer.Typer()
current_user = None
try:
    with open("./auth.json", "r") as file:
        user_info = json.load(file)

        user_info["_id"] = user_info["id"]
        del user_info["id"]

        current_user = make_user(**user_info)
except Exception as e:
    print(e)


@app.command("upload")
def main(filepath: Path):
    if current_user is None:
        return rich.print("[italic red]Você precisa se autenticar[/italic red]")

    if not filepath.is_file():
        rich.print("[red]O caminho passado não é um arquivo[/red]")
        return

    r2 = CloudflareR2Repository()
    repository = PeeweeFileRepository()

    upload_use_case = UploadFileUseCase(repository, r2)
    upload_use_case.execute(
        {
            "filesize": os.path.getsize(filepath),
            "name": filepath.name,
            "filepath": filepath,
            "owner": current_user,
        }
    )


@app.command("download")
def download(file_id: str):
    if current_user is None:
        return rich.print("[italic red]Você precisa se autenticar[/italic red]")

    r2 = CloudflareR2Repository()
    repository = PeeweeFileRepository()
    shared_link_repository = PeeweeSharedLinkRepository()

    download_use_case = DownloadFileUseCase(
        repository, r2, shared_link_repository
    )
    result = download_use_case.execute(file_id, current_user)
    if result.is_err():
        rich.print("[italic red]O arquivo não foi encontrado[/italic red]")
        return


@app.command("auth")
def auth_login(username: str, password: str):
    repository = PeeweeUserRepository()

    login_use_case = LoginUserUseCase(repository)
    result = login_use_case.execute(username, password)

    if result.is_err():
        return rich.print("[italic red]Credenciais inválidas[/italic red]")

    with open("./auth.json", "w") as file:
        json.dump(UserMapper.to_dict(result.ok_value), file)
    return rich.print(
        f"[italic green]Logado com sucesso, bem vindo {result.ok_value.name}[/italic green]"
    )


if __name__ == "__main__":
    app()
