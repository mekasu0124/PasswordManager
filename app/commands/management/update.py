from app.utilities.json import JsonEngine
import click
from rich.console import Console

console = Console()

@click.command(name="update")
@click.option("--link", required=True, help="The link currently saved")
@click.option("--username", required=True, help="The username currently saved")
@click.option("--password", required=True, help="The new password currently saved.")
@click.option("--new-username", required=False, help="The new username you want to set")
@click.option("--new-password", required=False, help="The new password you want to set")
def update_entry(link: str, username: str, password: str, new_username: str, new_password: str):
    json_engine = JsonEngine()
    current_data = json_engine.list_all_entries()
    entry_to_update = None
    for entry in current_data:
        if entry["link"] == link and entry["username"] == username:
            entry_to_update = entry
            break
    if entry_to_update:
        if new_username:
            for entry in current_data:
                if entry["link"] == link and entry["username"] == new_username:
                    console.print("[bold #272123]That Username Already Exists[/bold #272123]")
                    return
            entry_to_update["username"] = new_username
        if new_password:
            entry_to_update["password"] = new_password
        result = json_engine.update_entry(entry_to_update, current_data)
        console.print(f"[bold #385d8d]{result}[/bold #385d8d]")
    else:
        console.print("[bold #272123]Entry not found.[/bold #272123]")