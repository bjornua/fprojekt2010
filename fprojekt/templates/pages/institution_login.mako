<%inherit file="/main.mako"/>
<h1>Projekt X</h1>
<form action="${url_for("institution_login")}" method="post">
    <fieldset>
        <legend>Institutions log-ind</legend>
% if "auth_fail" in errors:
        <p>Forkert kode, prøv igen</p>
% endif
        <label for="inst_code">Institutionskode:</label><br />
        <input name="password" type="password"/><br/>
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>
