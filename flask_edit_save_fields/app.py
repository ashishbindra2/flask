from flask import Flask,session,redirect,render_template,jsonify,request,flash,url_for
from db import mangas_list,update_manga_detail,get_manga_by_id
edit_app = Flask(__name__)

edit_app.secret_key = "5fff768017d32b6146dc4eb4027a9cea33b23a9e3cef5acb"

@edit_app.get("/")
def test():
    return "hi there"

@edit_app.get("/get_mangas")
def view_mangas():

    mangas = mangas_list()
    return render_template('edit_page_1.html',mangas=mangas, )

@edit_app.get("/get_manga_detail/<string:mid>")
def get_manga_detail(mid: str):
    print(mid)
    manga_details = get_manga_by_id(mid)
    manga_details['_id'] = str(manga_details['_id'])
    return jsonify((manga_details))


@edit_app.route('/manga_details/<string:mid>')
def view_manga_details(mid: str):
    manga_details = get_manga_by_id(mid)
    print(manga_details)
    return render_template('edit_page_2.html',manga_detail=manga_details, )

@edit_app.route('/update_manga_list', methods=['POST'])
def set_company():
    try:
        data = request.get_json()
        mid = data.get('mangaId')

        if mid is None or len(mid) == 0:
            return jsonify({"message": "Error occurred while saving data"}), 500
        manga_details = {
            "Manga series": data.get('mangaName'),
            "Author(s)": data.get('mangaAuthor'),
            "Publisher": data.get('mangaPublisher'),
            "Serialized": data.get('mangaSerialized')
        }
        print(manga_details)
        
        update_manga_detail(mid, manga_details)

        return jsonify({"message": "Data successfully saved"}), 200
    except Exception as e:
        print("ex", e)
        # If an error occurs, send an error response
        return jsonify({"message": "Error occurred while saving data", "error": str(e)}), 500

@edit_app.post('/update_manga')
def update_manga():
    mid = request.form.get('mangaId')
    try:

        print(mid, "mid")
        if mid is None or len(mid) == 0:
            flash("Error while geting if")
            return "error"
        
        manga_details = {
            "Manga series": request.form.get('mangaName'),
            "Author(s)": request.form.get('mangaAuthor'),
            "Publisher": request.form.get('mangaPublisher'),
            "Serialized": request.form.get('mangaSerialized')
        }

        update_manga_detail(mid, manga_details)

    except Exception as e:
        print("Error: ", e)
        flash("data is not Updated for some reason")
        # If an error occurs, send an error response
    return redirect(url_for('view_manga_details', mid=mid))

@edit_app.route('/edit_view_3')
def edit_view_3():
    mangas = mangas_list()

    return  render_template("edit_page_3.html",mangas = mangas)

# @edit_app.route('/edit_view_3')
# def update_manga():
#     mangas = mangas_list()

#     return  render_template("edit_page_3.html",mangas = mangas)

if __name__ == "__main__":
    edit_app.run(debug=True, host='0.0.0.0', port=7007)
