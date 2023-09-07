import requests
import pandas as pd
from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class Event:
    """Represents a single event with a name, date, and summary."""

    name: str
    date: str
    summary: str


@dataclass
class WebPageInfo:
    """Stores information about a webpage for event scraping."""

    city_id: str
    url: str
    article_tag: str
    article_class: str
    event_name_tag: str
    event_name_class: str
    event_time_tag: str
    event_time_class: str
    event_summary_tag: str
    event_summary_class: str


def load_config(city_id: str) -> WebPageInfo:
    """
    Load webpage configuration for a given city_id from the config.csv file.

    Args:
        city_id (str): The id of the city for which to load configuration.

    Returns:
        WebPageInfo: The configuration information as a WebPageInfo object.
    """
    city_config_df = pd.read_csv("./config.csv")

    # Check if city_id exists in the CSV
    if city_id not in city_config_df["city_id"].values:
        print()
        print(f"{city_id} not found in the configuration file.")
        print(f"Available cities are : {city_config_df['city_id'].values}")
        print()

    # Use .loc to directly access the first row matching the city_id
    filter_df = city_config_df["city_id"] == city_id
    city_config_dict = city_config_df.loc[filter_df].to_dict("records")[0]

    # Replace nan imported with None
    city_config_dict = {
        key: None if pd.isna(value) else value
        for key, value in city_config_dict.items()
    }

    return WebPageInfo(**city_config_dict)


def get_webpage_information(event, webpage_info:WebPageInfo) -> Event:
    """
    Extract event information from a webpage using provided selectors.

    Args:
        event: The event element from the webpage.

        webpage_info (WebPageInfo): Information about the webpage structure.

    Returns:
        Event: The extracted event information.
    """
    # Return None if empty
    name = event.find(webpage_info.event_name_tag, class_=webpage_info.event_name_class)
    date = event.find(webpage_info.event_time_tag, class_=webpage_info.event_time_class)
    summary = event.find(
        webpage_info.event_summary_tag, class_=webpage_info.event_summary_class
    )

    name = name.text.strip() if name != None else None
    date = date.text.strip() if date != None else None
    summary = summary.text.strip() if summary != None else None

    if summary != None:
        summary = " ".join(summary.split())

    return Event(name, date, summary)


def format_event_print(number: int, event_info: Event) -> None:
    """
    Format and print event information.

    Args:
        number (int): The event number for its list position.

        event_info (Event): The event information.
    """
    print()
    print(f"{number + 1}. {event_info.name} -> {event_info.date}")
    print()
    print(event_info.summary if event_info.summary != None else "")
    print()


def whats_on(city_id: str) -> None:
    """
    Scrapes and prints events happening in a city this week from a specified website.

    This function sends a GET request to the provided URL, extracts event
    details, and prints them in a structured format.

    Args:
        city_id (str): The ID of the city for which to scrape events.
    """
    webpage_info = load_config(city_id)

    # Send a GET request to the URL
    page = requests.get(webpage_info.url)

    # Parse the HTML content
    page_content = BeautifulSoup(page.content, "html.parser")

    # Find all event articles
    events = page_content.find_all(
        webpage_info.article_tag, class_=webpage_info.article_class
    )

    # Loop through each event and extract details
    for number, event in enumerate(events):
        event_info = get_webpage_information(event, webpage_info)

        # Print event details
        format_event_print(number, event_info)


if __name__ == "__main__":
    print()
    city_id = input("What city are you interested in?: ")
    whats_on(city_id)
