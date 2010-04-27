<%inherit file="/main_admin.mako"/>
<%!
    def title(kwargs):
        return kwargs["name"]
    def section(kwargs):
        return "other"
%>
% if "not_authorized" in input_errors:
<h1>Du er ikke autoriseret til at se denne resource</h1>
<p>For at ændre i din profil skal du være logget <a href="${url_for("index")}">ind</a></p>
% else:
<h1>Profilside for ${escape(db_name)}</h1>
<form action="${url_for("user_profile",id=id)}" method="post">
    <table id="userprofile">
        <tr>
            <td class="userprofile_col_attr"><label for="name">Navn:</label></td>
            <td class="userprofile_col_content"><input type="text" id="name" value=${esc_attr(name)} name="name" disabled /></td>
            <td rowspan="6" id="userprofile_image">
                <img src="/static/images/test-portr%C3%A6t.png" title=${esc_attr(name)} alt=${esc_attr(name)} />
            </td>
        </tr>
        <tr>
            <td class="userprofile_col_attr"><label for="email">Email:</label></td>
            <td class="userprofile_col_content">
                % if "email_empty" in input_errors:
                    <span class="error_message">Du glemte at udfylde din email</span><br />
                % endif
                % if "email_invalid" in input_errors:
                    <span class="error_message">Den udfyldte email er ugyldig</span><br />
                % endif
            <input type="text" id="email" value=${esc_attr(email)} name="email"/></td>
        </tr>
        <tr>
            <td colspan="2"><label>Udfyld kun nedenstående felter hvis du vil ændrer dit kodeord.</label></td>
        </tr>
        <tr>
            <td class="userprofile_col_attr"><label for="new_password">Nyt kodeord:</label></td>
            <td class="userprofile_col_content"><input type="password" id="new_password" name="new_password" autocomplete="off" /></td>
        </tr>
        <tr>
            <td class="userprofile_col_attr"><label for="new_password_repeat">Gentag nyt kodeord:</label></td>
            <td class="userprofile_col_content">
                % if "passwords_not_the_same" in input_errors:
                    <span class="error_message">Kodeordet er ikke ens i begge felter.</span><br />
                % endif
            <input type="password" id="new_password_repeat" name="new_password_repeat" autocomplete="off" /></td>
        </tr>
        <tr>
            <td colspan="2"><input type="submit" value="Gem ændringer"/></td>
        </tr>
    </table>
</form>
% endif
