<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body style="background-color: #d1f7d1; font-family: Arial, sans-serif; margin: 0; padding: 0;">
    <div class="container" style="max-width: 800px; margin: 50px auto; padding: 20px; background: #fdfdfd; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
        <h1 style="text-align: center; color: #2e7d32; font-size: 2.5em; margin-bottom: 20px;">Prediction Result</h1>
        <p style="font-size: 1.2em; color: #424242; margin-bottom: 20px;">
            <strong style="color: #1b5e20;">Predicted Disease:</strong> {{ prediction }}
        </p>

        <div style="text-align: center; margin-bottom: 20px;">
            <img src="{{ image_path }}" alt="Uploaded Image" style="max-width: 100%; height: auto; border: 2px solid #2e7d32; border-radius: 10px;">
        </div>
        <div id="result" style="margin-top: 20px; padding: 15px; background: #f1f8e9; border-left: 4px solid #66bb6a; border-radius: 5px;">
            <p style="font-size: 1.2em; color: #2e7d32; font-weight: bold;">
                Suggested Remedy:
            </p>
            <p style="font-size: 1em; color: #424242;">
                {{ remedy }}
            </p>
        </div>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="text-decoration: none; background: #4caf50; color: #ffffff; padding: 10px 20px; font-size: 1em; border-radius: 5px; box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); transition: background 0.3s ease;">
                Go Back
            </a>
        </div>
    </div>

</body>
</html>
