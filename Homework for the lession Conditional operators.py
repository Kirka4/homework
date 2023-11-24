a=(input('введите строку '))

match a:
	case "save": print("Сохранить")
	case "load": print("Загрузить")
	case _: print("Неизвестная операция")
