def centrar(windows, wLarg, wAlt):

    ecranLar = windows.winfo_screenwidth()
    ecraAlt = windows.winfo_screenheight()

    posx = ecranLar // 2 - wLarg // 2
    posy = ecraAlt // 2 - wAlt // 2

    return f"{wLarg}x{wAlt}+{posx}+{posy}"
