import importlib

if __name__ == "__main__":
    commands = []

    command_classes = [
        ("commands.count", "Count"),
        ("commands.add", "Add")
    ]

    for module_name, class_name in command_classes:
        try:
            module = importlib.import_module(module_name)
            command_class = getattr(module, class_name)

            instance = command_class()
            commands.append(instance)
        except Exception as e:
            print(f"error: {e}")

    if commands:
        commands[0].run()
        commands[1].run()