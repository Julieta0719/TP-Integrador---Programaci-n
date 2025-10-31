from rich.console import Console
from rich.theme import Theme

colores_aplicados = Theme({
    "titulo": "bold cyan",
    "opcion": "bold white",
    "advertencia": "bold red",
    "exito": "bold green",
    "info": "yellow",
})

console = Console(theme=colores_aplicados)
