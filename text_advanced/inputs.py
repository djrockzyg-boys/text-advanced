def selector(prompt: object = "", selected_prompt: object = "Selected Option"):
    ask = input(f"\x1b[38;5;111m{prompt} >> \x1b[0m")
    print(f"\x1b[F\x1b[K\x1b[38;5;4m{selected_prompt} ({ask})\x1b[0m")
    return ask