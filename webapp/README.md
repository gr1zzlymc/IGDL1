# Instagram Photo Fetcher Web App

This simple Flask web app allows you to paste an Instagram post URL and view the images contained in that post. It uses the [Instaloader](https://github.com/instaloader/instaloader) library.

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Then open <http://localhost:8000> in your browser.

## Deployment on Render

Create a new Web Service on [Render](https://render.com) and connect this repository. Render will use `render.yaml` to build and serve the app.

## Disclaimer

This project is not affiliated with or endorsed by Instagram. Use at your own risk and respect Instagram's Terms of Service.
