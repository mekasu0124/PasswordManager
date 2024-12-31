from app.utilities.json import JsonEngine
import click


@click.command(name="update")
@click.option("--link", required=True, help="The link currently saved")
@click.option("--username", required=True, help="The username currently saved")
@click.option("--password", required=True, help="The new password currently saved.")
@click.option("--new-username", required=False, help="The new username you want to set")
@click.option("--new-password", required=False, help="The new password you want to set")
def update_command(link: str, username: str, password: str, new_username: str, new_password: str):
    """
    Allows the user to update an existing entry for a given link and username.
    The link will remain unchanged, but the username and/or password can be updated.
    """

    json_engine = JsonEngine()

    current_data = json_engine.list_all_entries()

    entry_to_update = None
    
    for entry in current_data:
        if entry["link"] == link and entry["username"] == username:
            entry_to_update = entry
            break

    if entry_to_update:
        if password:
            entry_to_update["password"] = password

        if new_username:
            entry_to_update["username"] = new_username

        result = json_engine.update_entry(entry_to_update, current_data)

        click.echo(result)
    else:
        click.echo("Entry not found.")