"""
CLI Tabuladores
"""
import sys

import click

from lib.exceptions import MyAnyError
from perseo.app import create_app
from perseo.blueprints.puestos.tasks import exportar_xlsx

app = create_app()
app.app_context().push()


@click.group()
def cli():
    """Puestos"""


@click.command()
def exportar():
    """Exportar Puestos a un archivo XLSX"""

    # Ejecutar la tarea
    try:
        mensaje_termino, _, _ = exportar_xlsx()
    except MyAnyError as error:
        click.echo(click.style(str(error), fg="red"))
        sys.exit(1)

    # Mensaje de termino
    click.echo(click.style(mensaje_termino, fg="green"))


cli.add_command(exportar)
