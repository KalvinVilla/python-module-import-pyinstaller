import importlib
import commands  # Importer le package principal

if __name__ == "__main__":
    commands_list = []

    # Importer dynamiquement toutes les commandes listées dans `commands.__all__`
    for module_name in commands.__all__:
        try:
            module = importlib.import_module(module_name)
            class_name = module_name.split(".")[-1].capitalize()  # Ex: "commands.count" -> "Count"

            if hasattr(module, class_name):
                command_class = getattr(module, class_name)
                instance = command_class()
                commands_list.append(instance)
        except Exception as e:
            print(f"error: {e}")

    # Exécuter toutes les commandes trouvées
    for command in commands_list:
        command.run()
