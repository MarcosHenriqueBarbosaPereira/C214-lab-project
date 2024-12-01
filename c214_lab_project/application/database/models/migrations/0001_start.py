from c214_lab_project.application.database.db_mgt.postgresql import (
    database_connection,
)
from c214_lab_project.application.database.models.file_db import FileDB
from c214_lab_project.application.database.models.shared_link_db import (
    SharedLinkDB,
)
from c214_lab_project.application.database.models.user_db import UserDB

database_connection.db.create_tables([UserDB, FileDB, SharedLinkDB])
