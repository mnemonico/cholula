import shlex
import click
import logging
import ovapi.configuration.setup_loggers
from ovapi.apicalls.extract_to_db import main

logger = logging.getLogger(__name__)

toto = "sdsdss"


@click.group()
def cli():
    pass


@click.command()
@click.argument("folder", nargs=1, type=str)
@click.argument("environment", envvar="XDG_CURRENT_DESKTOP")
def cmd2(folder, environment):
    print("CMD 2")
    print(folder, environment)
    logger.debug("done cmd2")
    logger.info("done cmd2")
    logger.warning("done cmd2")
    logger.error("done cmd2")
    logger.fatal("done cmd2")
    main()


cli.add_command(cmd2)

if __name__ == "__main__":
    cli()
