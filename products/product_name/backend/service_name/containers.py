from dependency_injector import containers, providers
from service_name.service.auth_service import AuthService
from service_name.service.user_management_service import UserManagementService
from service_name.infrastructure.user_repository._postgresdb.postgres_user_repository import PostgresUserRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'service_name.controller.user_routes',
        ]
    )

    mongodb_user_repository = providers.Singleton(PostgresUserRepository)

    user_management_service = providers.Singleton(
        UserManagementService,
        user_repository=mongodb_user_repository
    )

    auth_service = providers.Singleton(AuthService)