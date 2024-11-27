from dependency_injector import containers, providers
from products.product_name.backend.service_name.service.auth_service import AuthService
from service_name.service.user_management_service import UserManagementService
from service_name.infrastructure.user_repository._mongodb.mongo_db_user_repository import MongoDBUserRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'controller.user_routes'
        ]
    )

    mongodb_user_repository = providers.Singleton(MongoDBUserRepository)

    user_management_service = providers.Singleton(
        UserManagementService,
        user_repository=mongodb_user_repository
    )
    auth_service = providers.Singleton(AuthService)