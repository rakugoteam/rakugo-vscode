import vscode
import os

ext = vscode.Extension(
	name="rakugo-vscode",
	display_name="Rakugo for VSCode",
	version="0.0.1",
	description=" Tools For Developing Games using Rakugo"
)

@ext.event
def on_active():
	return f"The Extension '{ext.name}' has started"


@ext.command()
def dummy():
	# todo remove in feature
	return vscode.window.show_info_message("This is dummy message")

@ext.command()
def get_path():
  return vscode.window.show_info_message(os.path.abspath("."))

@ext.command()
def add_rakugo_to_project():
	packages_json = vscode.json.dumps(
		[
			{
				"package":"rakugo",
				"repo": "https://github.com/rakugoteam/Rakugo",
				"version": "3.3.0",
				"installed_to": "Rakugo", 
				"update": "stable" # or keep/dev
			},
			{
				"package":"adventure",
				"repo": "https://github.com/rakugoteam/Adventure",
				"version": "0.2",
				"installed_to": "adventure",
				"update": "stable" # or keep/dev
			},
			{
				"package":"emojis",
				"repo": "https://github.com/rakugoteam/Emojis-For-Godot",
				"version": "1.2",
				"installed_to": "emojis-for-godot",
				"update": "stable" # or keep/dev
			},
			{
				"package":"material-icons",
				"repo": "https://github.com/rakugoteam/Godot-Material-Icons",
				"version": "1.2",
				"installed_to": "material-design-icons",
				"update": "stable" # or keep/dev
			}
		]
	)
	
	if not os.path.exists("./addons"):
			os.mkdir(path="./addons")

	file = open("./addons/packages.json", "w")
	file.write(packages_json)
	file.close()

	return vscode.window.show_info_message("Rakugo has been added to your project")

vscode.build(ext)