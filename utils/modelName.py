def getModelNameFromId(modelId: str) -> str:
    match modelId:
        case "gpt-4":
            return "GPT-4"
        case "gpt-3.5-turbo":
            return "GPT-3.5 Turbo"
        case _:
            return "Unknown"
