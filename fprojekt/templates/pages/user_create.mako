<%inherit file="/subpage.mako"/>
<%!
    def title(kwargs):
        return "Opret bruger"
    def section(kwargs):
        return "other"
%>
<h1>Opret ny bruger</h1>
<form action="${url_for("user_create",inst_id=inst_id)}" method="post">
% if "name_empty" in input_errors:
    <p>Du glemte at udfylde et navn</p>
% endif
    <label for="name">Navn:</label><br />
    <input type="text" value=${esc_attr(name)} id="name" name="name"/><br />
% if "email_empty" in input_errors:
    <p>Du glemte at udfylde din email</p>
% endif
% if "email_invalid" in input_errors:
    <p>Den udfyldte email er ugyldig</p>
% endif
    <label for="email">Email:</label><br />
    <input type="text" value=${esc_attr(email)} id="email" name="email"/><br />

    <input type="submit" value="Opret bruger" />
</form>
