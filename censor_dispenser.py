# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_email(email_one):
    return email_one.replace("learning algorithms", "algorithms")

print(censor_email(email_one))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censor_text(email):
    for term in proprietary_terms:
     email_two.replace(term, " ")

    return email_two

print(censor_text(email_two))