@echo off
echo Starting Flask app with Waitress...

waitress-serve --host=0.0.0.0 --port=5000 app:app