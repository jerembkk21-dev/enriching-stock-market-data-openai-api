import os
import pandas as pd
from openai import OpenAI

client = OpenAI()

nasdaq100_ca = pd.read_csv(
    "nasdaq100_CA.csv"
)

price_change = pd.read_csv(
    "nasdaq100_price_change.csv"
)

nasdaq100_ca = nasdaq100_ca.merge(
    price_change[["symbol", "ytd"]],
    on="symbol"
)

sectors = [
    "Technology",
    "Consumer Cyclical",
    "Industrials",
    "Utilities",
    "Healthcare",
    "Communication",
    "Energy",
    "Consumer Defensive",
    "Real Estate",
    "Financial"
]

sector_results = []

for company in nasdaq100_ca["name"]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"""
                Classify the following company into exactly one of these sectors:

                {sectors}

                Company: {company}

                Return only the sector name.
                """
            }
        ]
    )

    sector_results.append(response.choices[0].message.content.strip())

nasdaq100_ca["sector"] = sector_results

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": f"""
            Here is information about Nasdaq companies:

            {nasdaq100_ca.to_string(index=False)}

            Recommend the two best sectors and at least two companies in each sector.
            Provide a brief summary explaining your recommendations.
            """
        }
    ]
)

stock_recommendations = response.choices[0].message.content.strip()

print(stock_recommendations)