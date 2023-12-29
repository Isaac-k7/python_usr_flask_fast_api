import uvicorn
import argparse
import services.fast_api as fast_api
import services.flask_api as flask_api

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Launch an API service")

    # Add named arguments
    parser.add_argument('--server', type=str, help="Choose the API service", default='flask', choices=['flask', 'fast_api'])

    # Parse command line arguments
    args = parser.parse_args()

    if args.server == "flask":
        flask_api.app.run(debug=True, host="127.0.0.1", port=5000)
    else:
        uvicorn.run(fast_api.app, host="127.0.0.1", port=8000)
