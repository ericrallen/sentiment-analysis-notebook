from typing import TypedDict

from .modelName import getModelNameFromId

Story = TypedDict(
    "Story",
    {
        "title": str,
        "time": int,
        "sentiment": TypedDict(
            "Sentiments",
            {
                "vaderStr": str,
                "vaderVal": float,
                "nrclex": str,
                "openai": dict[str, str],
            },
        ),
        "guard": TypedDict(
            "LakeraGuardResults",
            {
                "categories": TypedDict(
                    "LakeraGuardCategories",
                    {
                        "prompt_injection": bool,
                        "jailbreak": bool,
                        "sex": bool,
                        "hate": bool,
                        "pii": bool,
                        "unknown_links": bool,
                        "relevant_language": bool,
                    },
                ),
                "category_scores": TypedDict(
                    "LakeraGuardCategoryScores",
                    {
                        "prompt_injection": float,
                        "jailbreak": float,
                        "sex": float,
                        "hate": float,
                        "pii": float,
                        "unknown_links": float,
                        "relevant_language": float,
                    },
                ),
                "flagged": bool,
                "payload": dict[str, str],
                "pii": str,
                "links": list[str],
            },
        ),
    },
)

StoryData = dict[int, Story]


def collateSentimentData(stories: StoryData, model: str) -> dict[str, list[str]]:
    sentimentData: dict[str, list[str]] = {
        "Story": [],
        "VADER (String)": [],
        "VADER (Value)": [],
        "NRC": [],
        "ChatGPT (Sentiment String)": [],
        "ChatGPT (Sentiment Value)": [],
        "ChatGPT (Emotion)": [],
        "Zero Shot": [],
        "One Shot": [],
        "Few Shot": [],
    }

    try:
        for _, story in stories.items():
            if "title" in story:
                sentimentData["Story"].append(story["title"])

            if "vaderStr" in story["sentiment"]:
                sentimentData["VADER (String)"].append(story["sentiment"]["vaderStr"])

            if "vaderVal" in story["sentiment"]:
                sentimentData["VADER (Value)"].append(story["sentiment"]["vaderVal"])

            if "nrclex" in story["sentiment"]:
                sentimentData["NRC"].append(story["sentiment"]["nrclex"])

            if "openai" in story["sentiment"] and model in story["sentiment"]["openai"]:
                if "basic" in story["sentiment"]["openai"][model]:
                    sentimentData["ChatGPT (Sentiment String)"].append(
                        story["sentiment"]["openai"][model]["basic"]
                    )

                if "better" in story["sentiment"]["openai"][model]:
                    sentimentData["ChatGPT (Sentiment Value)"].append(
                        story["sentiment"]["openai"][model]["better"]
                    )

                if "advanced" in story["sentiment"]["openai"][model]:
                    sentimentData["ChatGPT (Emotion)"].append(
                        story["sentiment"]["openai"][model]["advanced"]
                    )

                if "emoji" in story["sentiment"]["openai"][model]:
                    sentimentData["Zero Shot"].append(
                        story["sentiment"]["openai"][model]["emoji"]
                    )

                if "oneshot" in story["sentiment"]["openai"][model]:
                    sentimentData["One Shot"].append(
                        story["sentiment"]["openai"][model]["oneshot"]
                    )

                if "fewshot" in story["sentiment"]["openai"][model]:
                    sentimentData["Few Shot"].append(
                        story["sentiment"]["openai"][model]["fewshot"]
                    )

        return sentimentData

    except NameError:
        print("Please run the cells above to gather and analyze some stories.")


def collateModelData(stories: StoryData) -> dict[str, list[str]]:
    modelData: dict[str, list[str]] = {"Story": []}

    try:
        for _, story in stories.items():
            if "openai" in story["sentiment"]:
                # if we only have one model result, we'll skip this story
                if not len(story["sentiment"]["openai"].keys()) > 1:
                    continue

                modelData["Story"].append(story["title"])

                for model, results in story["sentiment"]["openai"].items():
                    if model not in modelData:
                        modelName = getModelNameFromId(model)

                        if f"{modelName} (Sentiment String)" not in modelData:
                            modelData[f"{modelName} (Sentiment String)"] = []

                        if "basic" in results:
                            modelData[f"{modelName} (Sentiment String)"].append(
                                results["basic"]
                            )

                        if f"{modelName} (Sentiment Value)" not in modelData:
                            modelData[f"{modelName} (Sentiment Value)"] = []

                        if "better" in results:
                            modelData[f"{modelName} (Sentiment Value)"].append(
                                results["better"]
                            )

                        if f"{modelName} (Emotion)" not in modelData:
                            modelData[f"{modelName} (Emotion)"] = []

                        if "advanced" in results:
                            modelData[f"{modelName} (Emotion)"].append(
                                results["advanced"]
                            )

                        if f"{modelName} Zero Shot" not in modelData:
                            modelData[f"{modelName} Zero Shot"] = []

                        if "emoji" in results:
                            modelData[f"{modelName} Zero Shot"].append(results["emoji"])

                        if f"{modelName} One Shot" not in modelData:
                            modelData[f"{modelName} One Shot"] = []

                        if "oneshot" in results:
                            modelData[f"{modelName} One Shot"].append(
                                results["oneshot"]
                            )

                        if f"{modelName} Few Shot" not in modelData:
                            modelData[f"{modelName} Few Shot"] = []

                        if "fewshot" in results:
                            modelData[f"{modelName} Few Shot"].append(
                                results["fewshot"]
                            )

        return modelData

    except NameError:
        print("Please run the cells above to gather and analyze some stories.")

    if not len(modelData["Story"]):
        print(
            "Error: Please rerun the ChatGPT example cells with each model and then rerun this cell."
        )


def collateSafetyData(stories: StoryData) -> dict[str, list[str]]:
    safetyData: dict[str, list[str]] = {
        "Story": [],
        "Flagged": [],
        "Prompt Injection": [],
        "Jailbreak": [],
        "Sexual Content": [],
        "Hate Speech": [],
        "PII": [],
        "Unknown Links": [],
        "Relevant Language": [],
    }

    try:
        for _, story in stories.items():
            if "guard" in story:
                safetyData["Story"].append(story["title"])

                if "flagged" in story["guard"]:
                    safetyData["Flagged"].append(story["guard"]["flagged"])

                if "category_scores" in story["guard"]:
                    if "prompt_injection" in story["guard"]["category_scores"]:
                        safetyData["Prompt Injection"].append(
                            story["guard"]["category_scores"]["prompt_injection"]
                        )

                    if "jailbreak" in story["guard"]["category_scores"]:
                        safetyData["Jailbreak"].append(
                            story["guard"]["category_scores"]["jailbreak"]
                        )

                    if "sex" in story["guard"]["category_scores"]:
                        safetyData["Sexual Content"].append(
                            story["guard"]["category_scores"]["sex"]
                        )

                    if "hate" in story["guard"]["category_scores"]:
                        safetyData["Hate Speech"].append(
                            story["guard"]["category_scores"]["hate"]
                        )

                    if "pii" in story["guard"]["category_scores"]:
                        safetyData["PII"].append(
                            story["guard"]["category_scores"]["pii"]
                        )

                    if "unknown_links" in story["guard"]["category_scores"]:
                        safetyData["Unknown Links"].append(
                            story["guard"]["category_scores"]["unknown_links"]
                        )

                    if "relevant_language" in story["guard"]["category_scores"]:
                        safetyData["Relevant Language"].append(
                            story["guard"]["category_scores"]["relevant_language"]
                        )

        return safetyData

    except NameError:
        print("Please run the cells above to gather and analyze some stories.")

    if not len(safetyData["Story"]):
        print("Error: Please rerun the Lakera Guard cell and then rerun this cell.")
