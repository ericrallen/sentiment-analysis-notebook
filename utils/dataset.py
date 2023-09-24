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
        for storyId, story in stories.items():
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
