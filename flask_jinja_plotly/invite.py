import jinja2
import datetime as dt

template = jinja2.Environment(
    loader = jinja2.FileSystemLoader("templates"),
    # autoescape=jinja2.select_autoescapeW
                                    
).get_template("invite_template.txt")

# data for injecting into jinja2 template
templateContext = {
    "todayStr": dt.datetime.now().strftime("%d-%b-%Y"),
    "recipientName": "",
    "evntDtStr": "21-Oct-2021",
    "venueStr": "the beach",
    "senderName": "Sanket",
}

guests = ["Aakav", "Aakesh", "Aarav","ashish","akash",
          "Advik", "Chaitanya", "Chandran", "Darsh"]

for names in guests:
    
    templateContext['recipientName'] = names
    # print(templateContext)
    inviteText = template.render(templateContext)
    # print(inviteText)
    with open(f"./invite/{names}.txt", mode="w") as f:
        f.write(inviteText)
        