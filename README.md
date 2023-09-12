# Whats On - Event Scraper

This Python script was developed to provide an easy and convenient way to stay informed about whats on in your city. It scrapes and displays information about events happening in various cities from a specified website, with customization options available through a configuration file. The current supported cities include Melbourne and Sydney.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can use this script, you'll need the following:

- Python 3.x installed on your system.
- The necessary Python packages installed. You can install them using `pip`:

  pip install requests pandas beautifulsoup4

Getting Started

    Clone or download this repository to your local machine.

    Navigate to the project directory:

    cd whats_on

    Install the required packages as mentioned in the Prerequisites section.

Usage

To use the Whats On - Event Scraper, follow these steps:

    Run the script by executing the following command in your terminal:

    python whats_on.py

    You will be prompted to enter the city you're interested in. Type the city name or ID (configured in config.csv) and press Enter.

    The script will then fetch event information from the specified website and display it in a structured format.

Configuration

The script uses a configuration file named config.csv to customize its behavior for different cities. This file includes the following columns:

    city_id: The unique identifier for the city.
    url: The URL of the website where event information is scraped.
    article_tag: The HTML tag that wraps each event article.
    article_class: The CSS class name of the event article.
    event_name_tag: The HTML tag that contains the event name.
    event_name_class: The CSS class name of the event name.
    event_time_tag: The HTML tag that contains the event date and time.
    event_time_class: The CSS class name of the event date and time.
    event_summary_tag: The HTML tag that contains the event summary.
    event_summary_class: The CSS class name of the event summary.

You can customize the configuration for different cities by adding or modifying entries in the config.csv file.
Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue. We welcome contributions and improvements.


You can modify this `README.md` to include specific details about your project, such as installation instructions, usage examples, and additional documentation as needed.

