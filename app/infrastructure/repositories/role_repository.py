from app.domain.shared.role import Role
from app.infrastructure.repositories.repository_base import RepositoryBase

class RoleRepository(RepositoryBase):

    def __init__(self):
        super(RoleRepository, self).__init__()
