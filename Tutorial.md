# flask

### First we need to install 
-  `pip install python-dotenv`

- Remember to keep your .env file secure and not share it publicly, as it may contain sensitive information like API keys or database connection strings.
- Additionally, do not include your .env file in version control systems. 
- Add it to your .gitignore file to ensure it is not accidentally committed to your repository.

Create `.env` in root directory and add enviroment variables

* eg `PASSWORD = "SECRATES"`
* loard envrioment varable using `load_dotenv()
` function
* And use it like this `Password = os.getenv('SECRET_KEY')`

Flask obtain request data from various sources such as query parameter(URL args), formdata or session.
1. URL Parameter (Querry Args)
2. Form Data (POST Request)
3. Session
4. Request Headers
5. Request Cookies
6. JSON Data (POST Request)

1. URL Parameters(Query Args)
  -------------------------
  - Extract data from the URL's query parameters.
  `from Flask import request`
  `@app.router('/endpoint', methods =['GET])`<br>
  `def endpoint():`<br>
  `    par_value = request.args.get('paran_have)`
  - Light weight, non-senstive data that can be easily passed in URL

2. Form Data(POST Request)
 -------------------------
 - Access data submitted through a form using a post request use for sensitive or larger amount of data that should not be visible in the URL.
 `  form_value = request.form.get('form_field_name')`

3. Session
 --------
 - Store and retrive data associated with a specific client's session
 - Use for storing user-soecific data that persists across multiple request with a session.

 `@app.route('/set_session', method = ['GET'])`<br>
 `  def set_session():`<br>
 `      session['key'] = 'value'`<br>
 `      return 'session data'`<br>
<br>

 `@app.route('/get_session', method = ['GET'])`<br>
 `  def get_session():`<br>
 `      value = session.get('key')'`<br>
 `      return f'session value : {value}'`<br>

 Note: Remeber to setup the flask app and configure the session(if needed) using 'app.config['serct_key'] for session security


4. Request Header
  ---------------
  - you can access various HTTP headers sent by the client using request handeler. Headers can contain important information such as user agent content type, authtivcation token etc
   `user_agent = request.headers.get('User_Agent')`
   `content_type = request.headers.get("Content-Type)`


5. Request Cookies
  ---------------
  Cookies are often used to store small piece of data on the client side, which can be sent with each request. You can access cookies using `request.cookies`
  <br>
  
  ` cookie_value = request.cookies.get("cookie_date)`

6. Json Data (Post request)
 -------------------------
 If the client sending data in JSOn Format (usually in the request body ) you can access it using request.get_JSON()
 `json_data = request.get_json()`

-------------------------------------------------------------------------------------------------------------------------

* URL PArameter:

 - Typically consideres less secure for sensitive data is visible in URL.
 - Always validate and ssatitize the data to prevent any malicious input

* Form Data(POST Request)
 - More secure than URL parameters as the data is sent in the request body and not visible in the URL. However ensure proper validation & sentization of the form data to orevent attack
 
* Session
 --------
 - Session can be secure when implemented cautious. Use secure pracrice for handling session data, like encrypting
 sensitive data setting data strong secrate key &  manage session timeout
 
* Request Header
 ---------------
 - Can contain sesitive information.So be cautious about data being set in header. Always validate & ensure the interity of header data

* Json Data (Post request)
 -------------------------
 json data is secure if handled properly. Ensure that validate & senstive inconing JSON data & use safe & control manner to prevent pa... security vanerabilty.

- No method is inheritly more secure than other 
- Validatiion ensure that the data provide by the user meet specific ceriteria or constraint such as forte, length render

## Sanitization of data
  -------------------
  - Santization involves removing or escaping potentially danger charaters or code from the input data to prevent security venarbilty.
  - proper :  it helps migrate risk such as SQL Injection & Cross-site scripting attack
  - Secial character that contain misinterprent in SQL Query eg single quotes

  ##### SQL Injection
  * malicious SQL code into an application input field expload vulnerabilty in the database layer
  ##### XSS -.=> Cross Site Scripting Attacks
  - XSS attacks involus injection malicous scripts (Usally javascript) into web applications that are then exrcuted in the users browsers, protentialy steeling sesntive data or perform malious attacks 

 `@app.route('/validate', method['POST'])`
    `def validate_date():`
        `user_input = request.foem.get('')`
        '# example validation: checking if the input is a None'
        `if not user_input.isdigit():`
            `retrun "Invalid Input"`
        # sanitized use bleah to clean HTML
        `sentized_input = bleach.clean(user_input)`