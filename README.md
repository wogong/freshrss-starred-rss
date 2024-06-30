## freshrss-starred

Atom feed exporter for FreshRSS starred items.

### Usage
1. `cp config.example.json config.json` and update `config.json` with your own values.
2. `pip install -r requirements`
3. `python app.py`, or you can deply using Docker or Docker Compose.
4. Serve at port 5000.

### Notes
- Showing most recent 20 starred items, can be modified if neccesarry.
- serve port can be altered in `app.py`.

### Credits
- Many code borrow from <https://git.mmk2410.org/mmk2410/freshrss2pocket>
- Inspired by <https://github.com/erdnaxe/miniflux-luma>