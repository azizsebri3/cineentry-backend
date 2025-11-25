import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Charger les variables depuis .env
from dotenv import load_dotenv
load_dotenv()

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importer Base depuis ton projet
# ⚠️ TRÈS IMPORTANT : on importe après load_dotenv
from app.database import Base

# Ici Alembic va trouver toutes les tables
target_metadata = Base.metadata

# Récupérer DATABASE_URL depuis ton .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Remplacer l'URL définie dans alembic.ini
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
