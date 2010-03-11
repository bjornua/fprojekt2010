<%inherit file="/main.mako"/>
<h1>Velkommen til Pedac</h1>
<form action="${url_for("user_login")}" method="post">
    <fieldset>
        <legend>Pædagog log-ind</legend>
        <label for="email">Email:</label><br />
        <input type="text" id="email" name="email"/><br />
        <label for="password">Adgangskode:</label><br />
        <input id="password" type="password" name="password"/><br />
        
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>
<form action="${url_for("institution_login")}" method="post">
    <fieldset>
        <legend>Institutions log-ind</legend>
        <label for="inst_code">Institutionskode:</label><br />
        <input name="password" type="password"/><br/>
        <input type="submit" value="Log ind!"/>
    </fieldset>
    <p>
        I tvivl? Ring til <strong>54 75 54 54</strong>
    </p>
</form>
<form action="${url_for("admin_login")}" method="post">
    <fieldset>
        <legend>Administrator log-ind</legend>
        <label for="username">Brugernavn:</label><br />
        <input type="text" id="username" name="username"/><br />
        <label for="password">Adgangskode:</label><br />
        <input type="password" id="password" name="password"/><br />
        <input type="submit" value="Log ind!"/>
    </fieldset>
</form>
