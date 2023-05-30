import click

from .utils import PathlibPath
from .._types import FuncType


schema: FuncType = click.option(
    '--schema',
    type=PathlibPath(exists=True, dir_okay=False, resolve_path=True),
    help='The location of the Prisma schema file.',
    required=False,
)

watch: FuncType = click.option(
    '--watch',
    is_flag=True,
    default=False,
    required=False,
    help='Watch the Prisma schema and rerun after a change',
)

generator: FuncType = click.option(
    '--generator',
    type=str,
    multiple=True,
    required=False,
    help='Specifies which generator to use to generate assets. This option may be provided multiple times to include multiple generators. By default, all generators in the target schema will be run.',
)

skip_generate: FuncType = click.option(
    '--skip-generate',
    is_flag=True,
    default=False,
    help='Skip triggering generators (e.g. Prisma Client Python)',
)
