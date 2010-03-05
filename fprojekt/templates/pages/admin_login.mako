<%inherit file="/main.mako"/>
<h1>Projekt X</h1>
<form action="${url_for("admin_login")}" method="post">
    <fieldset>
        <legend>Administrator log-ind</legend>
        <label for="username">Brugernavn:</label><br />
        <input type="text" id="username" name="username"/><br />
        <label for="password">Adgangskode:</label><br />
        <input id="password" type="password" name="password"/><br />
        
        <input type="submit" value="Log ind!"/>
    </fieldset>
</form>
