# MusicLinkConverter

A program to convert between Tidal and Spotify links. Maybe I'll add other platforms, but I don't really have the need for any other platforms for now. 

Pass in as an argument either a Tidal or Spotify link to a song. The converted link will be printed to stdout.

## Getting Started

To get started, clone this repository by running `git clone https://github.com/FlynnD273/MusicLinkConverter` or download a zip file of the repository.

You must have python 3 and pip installed. To install all dependencies, run `pip install -r requirements.txt`

Then run `python convert.py <URL GOES HERE>`


To search for a single track on Spotify, run `python search-spotify.py <SEARCH TERM HERE>`.
This will print the URL to the top result.

Similarly, you can run `python search-tidal.py <SEARCH TERM HERE>` to search Tidal.
