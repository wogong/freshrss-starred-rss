# FreshRSS Starred Items Exporter

An Atom feed exporter for FreshRSS starred items.

## Features

- Exports the most recent 20 starred items from FreshRSS
- Serves the feed on port 5000 by default
- Easily configurable and deployable

## Prerequisites

- Python 3.x
- FreshRSS instance with API access

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/wogong/freshrss-starred.git
   cd freshrss-starred
   ```

2. Copy the example configuration file and update it with your FreshRSS details:
   ```
   cp config.example.json config.json
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

Start the application:

```
python app.py
```

The feed will be available at `http://localhost:5000`.

### Docker Deployment

You can also deploy using Docker or Docker Compose (instructions to be added).

## Configuration

Edit `config.json` to set the following parameters:

- `freshrss_url`: Your FreshRSS instance URL
- `freshrss_username`: Your FreshRSS user name
- `freshrss_api_password`: Your FreshRSS API password

## Customization

- To modify the number of starred items shown, edit the relevant variable in `app.py`.
- The server port can be changed in `app.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- Code partially adapted from [freshrss2pocket](https://git.mmk2410.org/mmk2410/freshrss2pocket)
- Inspired by [miniflux-luma](https://github.com/erdnaxe/miniflux-luma)
