This is flask Auth Guid 
---

In a terminal, you can set the FLASK_APP and FLASK_DEBUG values:
`export FLASK_APP=project
export FLASK_DEBUG=1
`
- Environment Variable:
    - Set the FLASK_APP environment variable to your app's name and run with the flask run command:
    - On Windows, use set instead of export.
    - `set FLASK_APP=project`
    - `set FLASK_DEBUG=1`

To run flask file
---
1. python app.py
    1. python app.py --host=0.0.0.0 --port=8080
2. export FLASK_APP=app
    - `flask run`
3. python your_script.py runserver
4. flask --app hello run
    - hello file name
    - app is instance
 