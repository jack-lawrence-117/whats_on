# Whats On - Event Scraper

This Python script was developed as a quick weekend project, aiming to offer a simple and convenient solution for staying informed about events in your city. It efficiently scrapes and presents event information from a specified website, and enables users to easily introduce their own city through the configuration file. Currently, the supported cities include Melbourne and Sydney.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites

Before you can use this script, you'll need the following:

- Python 3.x installed on your system.
- The necessary Python packages installed. You can install them using `pip`:

  pip install requests pandas beautifulsoup4

## Getting Started

- Clone or download this repository to your local machine.

- Navigate to the project directory:

- cd whats_on

- Install the required packages as mentioned in the Prerequisites section.

## Usage

To use the Whats On, follow these steps:

Run the script by executing the following command in your terminal:

    python whats_on.py

You will be prompted to enter the city you're interested in. Type the city name or ID (configured in config.csv) and press Enter.

The script will then fetch event information from the specified website and display it in a structured format.

## Configuration

The script uses a configuration file named config.csv to identify what portions of the website relate to what tags and classes. 

This file includes the following columns:

    city_id: The unique identifier for the city.
    url: The URL of the website where event information is scraped.
    *_tag: The HTML tag locating the name, time or summary text. 
    *_class: The CSS class locating the name, time or summary text. 
    
To add more cities or adjust the current displayed content, simply edit the entries in the config.csv file.
