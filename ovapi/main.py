import logging

import click

import ovapi.configuration.setup_loggers

# from ovapi.apicalls.extract_to_db import main

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@click.command()
@click.argument("folder", nargs=1, type=str)
@click.argument("environment", envvar="XDG_CURRENT_DESKTOP")
def cmd2(folder, environment):
    logger.debug(environment)
    # logger.debug(folder)
    logger.info(environment)
    logger.warning(environment)
    logger.error(environment)
    logger.fatal(environment)
    # main()


cli.add_command(cmd2)

if __name__ == "__main__":
    cli()
