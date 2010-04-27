<%inherit file="/main_admin.mako"/>
<%!
    def title(kwargs):
        return "Opret institution"
    def section(kwargs):
        return "other"
%>
<h1>Opret ny institution</h1>
<form action="${url_for("institution_create")}" method="post">
% if "name_empty" in input_errors:
    <p>Du glemte at udfylde et navn</p>
% endif
    <label for="name">Navn:</label><br />
    <input type="text" value=${esc_attr(name)} id="name" name="name"/><br />
% if "phone_empty" in input_errors:
    <p>Du glemte at udfylde et telefonnummer</p>
% endif
    <label for="phone">Telefon:</label><br />
    <input type="text" value=${esc_attr(phone)} id="phone" name="phone"/><br />
% if "email_empty" in input_errors:
    <p>Du glemte at udfylde din email</p>
% endif
% if "email_invalid" in input_errors:
    <p>Den udfyldte email er ugyldig</p>
% endif
    <label for="email">Email:</label><br />
    <input type="text" value=${esc_attr(email)} id="email" name="email"/><br />

    <input type="submit" value="Opret institution" />
</form>
